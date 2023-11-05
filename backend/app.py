import requests
from flask import Flask, jsonify

app = Flask(__name__)

ANKI_CONNECT_URL = "http://localhost:8765"

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

@app.route('/get_cards_reviews/<deck_name>')
def get_cards_reviews(deck_name):
    try:
        # Get all card IDs from the specified deck
        card_ids_response = anki_connect_invoke('findCards', {'query': f'deck:"{deck_name}"'})
        card_ids = card_ids_response.get('result', [])
        
        if not card_ids:
            return jsonify({'error': 'No cards found in the specified deck'}), 404
        
        # Get cards info in a single batch request instead of one by one
        card_info_response = anki_connect_invoke('cardsInfo', {'cards': card_ids})
        card_infos = card_info_response.get('result', [])
        
        # Prepare a dict to hold ease of each card
        card_eases = {}
        
        # Get review details for all cards in one request
        reviews_response = anki_connect_invoke('getReviewsOfCards', {'cards': card_ids})
        reviews = reviews_response.get('result', {})
        
        for card_id, review in reviews.items():
            if review:  # Ensure there is a review, otherwise, it could be a new card
                card_eases[card_id] = review[-1]['ease']
        
        cards_data = [{
            'card_id': card_info['cardId'],
            'front': card_info['fields']['Front']['value'],
            'back': card_info['fields']['Back']['value'],
            'ease': card_eases.get(str(card_info['cardId']), None)  # Use .get() to handle cards without reviews
        } for card_info in card_infos]

        return jsonify(cards_data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
