from typing import Dict, Any
from models.models import Deck
import json
from json import JSONDecodeError


def handler(event: Dict[str, Any], _: Any) -> Dict[str, Any]:
    try:
        params = event["queryStringParameters"]
        deck_id = params.get("deckId", None)
        user_id = params.get("userId", None)
        
        if deck_id:
            try:
                deck = Deck.get(user_id, deck_id)
                return {
                    "statusCode": 200,
                    "body": json.dumps(dict(deck.attribute_values))
                }
            except Deck.DoesNotExist as e:
                return {
                    "statusCode": 404
                }
        else:
            try:

                decks = [dict(deck.attribute_values) for deck in Deck.query(user_id)]
                return {
                    "statusCode": 200,
                    "body": json.dumps(decks)
                }
            except Exception as e:
                raise e
    except KeyError as e:
        return {
            "statusCode": 400,
            "message": str(e)
        }

