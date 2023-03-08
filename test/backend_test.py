import requests as req

URL = "https://77x0u4uueb.execute-api.us-east-1.amazonaws.com/prod"
TEST_USER_ID = "user-for-tests"
TEST_DECK_ID = "f520d196-89cb-4947-b1fc-ac838e9c8899"


def test_get_deck_or_all_decks(deckId=None):
    url = f"{URL}/decks/?userId={TEST_USER_ID}"
    if deckId:
        url += f"&deckId={deckId}"

    response = req.get(url)

    assert response.status_code == 200

    if deckId:
        cards = response.json()["cards"]
        assert len(cards) == 2
    else:
        cards_from_a = response.json()[0]["cards"]
        cards_from_b = response.json()[0]["cards"]
        assert len(cards_from_a) == 2 and len(cards_from_b) == 2

def test_create_deck():
    deckName = "test-deck-0"
    deckId =


if __name__ == "__main__":
    test_get_deck_or_all_decks()
