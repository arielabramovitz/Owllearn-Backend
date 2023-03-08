from typing import Dict, Any
import json
from json import JSONDecodeError
from models.models import Card, Deck, DeckPreview


def handler(event: Dict[str, Any], _: Any) -> Dict[str, Any]:
    try:
        
        body = json.loads(event['body'])
        deck = body["deck"]
        deck_preview = body["deckPreview"]

        
        new_cards = deck["cards"]
        prevDeck = Deck.get(deck["userId"], deck["deckId"])
        old_cards = prevDeck.cards

        deleted = [({"deckId": card["deckId"], "cardId": card["cardId"]}, card["ranking"]) for card in old_cards if card not in new_cards]
        created = [Card(deckId= card["deckId"], cardId= card["cardId"], front= card["front"], back=card["back"]) for card in new_cards if card not in old_cards]
        deckPreview = DeckPreview.get(prevDeck.userId, prevDeck.deckId)


        for card, ranking in deleted:
                deckPreview.decrement_rank(ranking)
                c = Card.get(card["deckId"], card["cardId"])
                c.delete()
        with Card.batch_write() as batch:
            
            for card in created:
                deckPreview.unmarked += 1
                batch.save(card)

        deckPreview.save()
        
        prevDeck.cards = new_cards
        prevDeck.save()

        
        return {
            "statusCode": 200,
            "body": json.dumps(dict(prevDeck.attribute_values))
        }
    except Exception as e:
        print(e)
        return {
            "statusCode": 500
        }
