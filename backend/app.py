# app.py

from flask import Flask, jsonify
from anki_tools import get_cards_review_details

app = Flask(__name__)

@app.route('/get_cards_reviews/<deck_name>')
def get_cards_with_topics(deck_name):
    try:
        nested_cards_data = get_cards_review_details(deck_name)
        if 'error' in nested_cards_data:
            return jsonify(nested_cards_data), nested_cards_data.get('status', 500)
        return jsonify(nested_cards_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
