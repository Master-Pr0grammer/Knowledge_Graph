# test_anki_tools.py

from anki_tools import get_cards_review_details

def test_get_cards_review_details(deck_name):
    result = get_cards_review_details(deck_name)
    print("Resulting Nested Dictionary: ")
    print(result)
    return result

if __name__ == "__main__":
    # Use a test deck name here, or prompt for user input
    test_deck_name = "Biology - Biochemistry"  # Replace with a real deck name
    test_get_cards_review_details(test_deck_name)
