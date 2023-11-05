# Anki Reviews Flask API

This Flask API serves as an intermediary between clients and AnkiConnect, enabling the retrieval of Anki card reviews from a specified deck. It is designed to work with the AnkiConnect plugin, which allows external applications to communicate with Anki.

## Features

- Retrieve Anki card reviews for a specific deck.
- Get front and back of cards along with their ease factors.
- Filter cards by the specified deck name.

## Prerequisites

To use this API, you need to have:

- [Anki](https://apps.ankiweb.net/) installed on your system.
- The [AnkiConnect](https://foosoft.net/projects/anki-connect/index.html) plugin added to Anki.

## Setup

Follow these steps to set up the Flask API on your local machine:

### Install Anki and AnkiConnect

1. Install Anki from the official [download page](https://apps.ankiweb.net/).
2. Open Anki and install the AnkiConnect add-on by following the instructions on its [AnkiWeb page](https://ankiweb.net/shared/info/2055492159).

### Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/your-github/anki-reviews-api.git
cd anki-reviews-api
```

### Setting up a virtual environment
Create a virtual environment to manage dependencies:

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Once you have the venv, pip install -r requirements

### Running the app
python ./app.py to run
GET request /get_cards_reviews/<deck_name>


### Planning
-One dictionary containing the front and back