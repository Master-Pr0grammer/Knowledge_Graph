# test_anki_tools.py

from anki_tools import get_cards_review_details, get_cards_with_topics

def test_get_cards_review_details(deck_name):
    result = get_cards_review_details(deck_name)
    other_result = get_cards_with_topics(deck_name)
    print("Resulting Nested Dictionary: ")
    print(result)
    print("Other Resulting Nested Dictionary: ")
    print(other_result)
    return result

if __name__ == "__main__":
    # Use a test deck name here, or prompt for user input
    test_deck_name = "Biology - Biochemistry"  # Replace with a real deck name
    test_get_cards_review_details(test_deck_name)
