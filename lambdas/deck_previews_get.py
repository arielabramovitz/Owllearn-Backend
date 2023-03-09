from typing import Dict, Any
import json
from json import JSONDecodeError
from models.models import DeckPreview


def handler(event: Dict[str, Any], _: Any) -> Dict[str, Any]:
    try:
        params = event["queryStringParameters"]
        deck_id = params.get("deckId", None)
        user_id = params.get("userId", None)
        
        if deck_id:
            deck_preview = DeckPreview.get(user_id, deck_id)
            deck_p = {
                "deckName": deck_preview.deckName,
                "unmarked": deck_preview.unmarked,
                "easy": deck_preview.easy,
                "medium": deck_preview.medium,
                "hard": deck_preview.hard,
                "deckId": deck_preview.deckId,
                "userId": deck_preview.userId
            }
            return {
                "statusCode": 200,
                "body": json.dumps(deck_p)
            }
        else:
            previews = [dict(prev.attribute_values) for prev in DeckPreview.query(user_id)]
            return {
                "statusCode": 200,
                "body": json.dumps(previews)
            }
                
    except DeckPreview.DoesNotExist as e:
        return {
            "statusCode": 400,
            "message": str(e)
        }
    except (KeyError, ValueError) as e:
        return {
            "statusCode": 400,
            "message": str(e)
        }