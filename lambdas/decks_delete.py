from typing import Dict, Any
from models.models import Deck, Card, DeckPreview


def handler(event: Dict[str, Any], _: Any) -> Dict[str, Any]:
    try:
        params = event["queryStringParameters"]
        deck_id = params.get("deckId", None)
        user_id = params.get("userId", None)
        
        deck = Deck.get(user_id, deck_id)
        
        cards = Card.query(deck_id)
        
        for card in cards:
            card.delete()
        
        deckPreview = DeckPreview.get(user_id, deck_id)
        deckPreview.delete()
        deck.delete()
        
        return {
            "statusCode": 200
        }
        
    except Exception as e:
        raise e
