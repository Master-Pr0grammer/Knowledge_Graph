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

@app.route('/get_cards_reviews')
def get_cards_reviews():
    try:
        # Get all card IDs
        card_ids_response = anki_connect_invoke('findCards', {'query': ''})  # Empty query for example
        card_ids = card_ids_response.get('result', [])
        
        if not card_ids:
            return jsonify({'error': 'No cards found'}), 404
        
        # Get review details for each card
        reviews_response = anki_connect_invoke('getReviewsOfCards', {'cards': card_ids})
        reviews = reviews_response.get('result', {})

        cards_data = []
        for card_id in card_ids:
            # Get cards info
            card_info_response = anki_connect_invoke('cardsInfo', {'cards': [card_id]})
            card_info = card_info_response.get('result', [{}])[0]

            front = card_info['fields']['Front']['value']
            back = card_info['fields']['Back']['value']
            card_ease = reviews[str(card_id)][-1]['ease'] if str(card_id) in reviews and reviews[str(card_id)] else None

            card_data = {
                'card_id': card_id,
                'front': front,
                'back': back,
                'ease': card_ease
            }
            cards_data.append(card_data)

        return jsonify(cards_data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

# def anki_connect_invoke(action, params=None, version=6):
#     request_data = {
#         'action': action,
#         'params': params or {},
#         'version': version
#     }
#     response = requests.post(ANKI_CONNECT_URL, json=request_data)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         raise ConnectionError(f"AnkiConnect call failed: {response.text}")

# @app.route('/get_cards_reviews')
# def get_cards_reviews():
#     try:
#         # Get all card IDs
#         card_ids_response = anki_connect_invoke('findCards', {'query': ''})  # Empty query for example
#         card_ids = card_ids_response.get('result', [])
        
#         if not card_ids:
#             return jsonify({'error': 'No cards found'}), 404
        
#         # Get review details for each card
#         reviews_response = anki_connect_invoke('getReviewsOfCards', {'cards': card_ids})
#         reviews = reviews_response.get('result', {})

#         cards_data = []
#         for card_id in card_ids:
#             # Get cards info
#             card_info_response = anki_connect_invoke('cardsInfo', {'cards': [card_id]})
#             card_info = card_info_response.get('result', [{}])[0]

#             front = card_info['fields']['Front']['value']
#             back = card_info['fields']['Back']['value']
#             card_ease = reviews[str(card_id)][-1]['ease'] if str(card_id) in reviews and reviews[str(card_id)] else None

#             card_data = {
#                 'card_id': card_id,
#                 'front': front,
#                 'back': back,
#                 'ease': card_ease
#             }
#             cards_data.append(card_data)

#         return jsonify(cards_data)

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# if __name__ == "__main__":
#     app.run(debug=True)
