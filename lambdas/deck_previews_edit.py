from typing import Dict, Any
from models.models import Deck, DeckPreview
import json
from json import JSONDecodeError

def handler(event: Dict[str, Any], _: Any) -> Dict[str, Any]:
    try:
        body = json.loads(event['body'])
        previews = body["previews"]
        for prev in previews:
            oldPrev = DeckPreview.get(prev["userId"], prev["userId"])
            oldPrev.unmarked = prev["unmarked"]
            oldPrev.easy = prev["easy"]
            oldPrev.medium = prev["medium"]
            oldPrev.hard = prev["hard"]
            oldPrev.save()
        return {
            "statusCode": 200
        }
            
    except (JSONDecodeError, DeckPreview.DoesNotExist, KeyError, ValueError) as e:
        return {
            "statusCode": 500
        }
