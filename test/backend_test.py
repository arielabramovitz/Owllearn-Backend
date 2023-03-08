import json

import requests as req

URL = "https://77x0u4uueb.execute-api.us-east-1.amazonaws.com/prod"
TEST_USER_ID = "user-for-tests"
TEST_DECK_ID = "a2b2a22d-b2d4-48b8-8a78-63faced24490"


def test_get_deck_or_all_decks(deckId=None):
    url = f"{URL}/decks/?userId={TEST_USER_ID}"
    if deckId:
        url += f"&deckId={deckId}"

    response = req.get(url)

    assert response.status_code == 200

def test_create_deck():
    deckName = "test-deck-0"
    url = f"{URL}/decks/"
    body = {
        "userId": TEST_USER_ID,
        "deckId": deckName,
        "deckName": deckName
    }
    response = req.post(url, json=body)
    assert response.status_code == 201

def test_delete_deck():
    deckName = "test-deck-0"
    url = f"{URL}/decks/?userId={TEST_USER_ID}&deckId={deckName}"

    response = req.delete(url)
    assert response.status_code == 200

def test_edit_deck():
    url = f"{URL}/decks/"
    body = {
        "deck": {
            "userId": "user-for-tests",
            "deckId": "a2b2a22d-b2d4-48b8-8a78-63faced24490",
            "deckName": "test 1",
            "cards": [{"cardId": "0fd8a145-ab40-4018-afff-3fbebb997b77", "deckId": "a2b2a22d-b2d4-48b8-8a78-63faced24490", "front": "asdasd", "back": "asdasd", "ranking": "unmarked"}]
        },
        "deckPreview": {
            "userId": "user-for-tests",
            "deckId": "a2b2a22d-b2d4-48b8-8a78-63faced24490",
            "deckName": "test 1",
            "unmarked": 0,
            "easy": 1,
            "medium": 0,
            "hard": 0
        }

    }
    response = req.put(url, json=body)
    assert response.status_code == 200


if __name__ == "__main__":
    test_get_deck_or_all_decks()
    test_create_deck()
    test_delete_deck()
    test_edit_deck()