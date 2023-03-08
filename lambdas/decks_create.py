from typing import Dict, Any
from models.models import Deck, DeckPreview
import json
from json import JSONDecodeError
from pynamodb.exceptions import PutError

def handler(event: Dict[str, Any], _: Any) -> Dict[str, Any]:
    
    
    try:
        body = json.loads(event['body'])
        deck_id = body['deckId']
        user_id = body['userId']
        deck_name = body['deckName']
        deck = Deck(userId=user_id, deckId=deck_id, deckName=deck_name).save()
        deck_preview = DeckPreview(userId=user_id, deckId=deck_id, deckName=deck_name).save()
        return {
            "statusCode": 200,
            "body": json.dumps(dict(deck.attribute_values))
        }
    except (PutError, JSONDecodeError, TypeError, KeyError) as e:
        return {
            "statusCode": 500
        }
    
    
    
