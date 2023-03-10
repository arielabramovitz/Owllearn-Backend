from typing import Dict, Any
from models.models import Card, DeckPreview, Deck
import json
from json import JSONDecodeError

def handler(event: Dict[str, Any], _: Any) -> Dict[str, Any]:
    try:
        body = json.loads(event['body'])
        user_id = body["deckPreview"]["userId"]
        deck_id = body["deckPreview"]["deckId"]
        cards = body.get("cards", None)
        deck = Deck.get(user_id, deck_id)
        deckPreview = DeckPreview.get(user_id, deck_id)
        deckPreview.unmarked = body["deckPreview"]["unmarked"]
        deckPreview.easy = body["deckPreview"]["easy"]
        deckPreview.medium = body["deckPreview"]["medium"]
        deckPreview.hard = body["deckPreview"]["hard"]
        
        rankings = {card["cardId"]: card["ranking"] for card in cards}
        
        if cards:                
            for card in deck.cards:
                if rankings.get(card["cardId"], None):
                    card["ranking"] = rankings[card["cardId"]]
                    c = Card.get(deck_id, card["cardId"])
                    c.ranking = card["ranking"]
                    c.save()
            deck.save()
                
        deckPreview.save()
        return {
            "statusCode": 200,
            "body": json.dumps(dict(deckPreview.attribute_values))
        }
            
    except (JSONDecodeError, DeckPreview.DoesNotExist, KeyError, ValueError) as e:    
        return {
            "statusCode": 500
        }
