# anki_tools.py

import requests
import re
from categorization import generate_category

ANKI_CONNECT_URL = "http://localhost:8765"

def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def anki_connect_invoke(action, params=None, version=6):
    request_data = {
        'action': action,
        'params': params or {},
        'version': version
    }
    response = requests.post(ANKI_CONNECT_URL, json=request_data)
    if response.status_code == 200:
        return response.json()
    else:
        raise ConnectionError(f"AnkiConnect call failed: {response.text}")

def get_cards_review_details(deck_name):
    card_ids_response = anki_connect_invoke('findCards', {'query': f'deck:"{deck_name}"'})
    card_ids = card_ids_response.get('result', [])
    
    if not card_ids:
        return {'error': 'No cards found in the specified deck'}, 404
    
    card_info_response = anki_connect_invoke('cardsInfo', {'cards': card_ids})
    card_infos = card_info_response.get('result', [])
    
    card_eases = {}
    reviews_response = anki_connect_invoke('getReviewsOfCards', {'cards': card_ids})
    reviews = reviews_response.get('result', {})
    
    for card_id, review in reviews.items():
        # Scale ease from 0-4 to 0-100
        card_eases[card_id] = 25 * (review[-1]['ease'] if review else 0)
    
    nested_cards_data = {}
    
    for card_info in card_infos:
        front = remove_html_tags(card_info['fields']['Front']['value'])
        back = remove_html_tags(card_info['fields']['Back']['value'])
        card_key = f"{front} {back}"
        
        # Ensure the score is within the new scale of 0-100
        score = card_eases.get(str(card_info['cardId']), 0)
        score = 0 if score < 0 else 100 if score > 100 else score
        
        nested_cards_data[card_key] = {
            "topics": [deck_name],
            "score": score
        }
    
    return nested_cards_data

def get_cards_with_topics(deck_name):
    raw_dict = get_cards_review_details(deck_name)
    
    # Check if there was an error retrieving card details
    if 'error' in raw_dict:
        return raw_dict
    
    gpt_dict = dict((k, v["topics"]) for k, v in raw_dict.items())
    gpt_output_dict = generate_category(gpt_dict)
    
    new_dict = raw_dict.copy()

    for key in raw_dict.keys():
        new_dict[key]["topics"] = gpt_output_dict[key]
    
    return new_dict