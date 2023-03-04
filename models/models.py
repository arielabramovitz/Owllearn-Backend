import os

from pynamodb.attributes import UnicodeAttribute, MapAttribute, NumberAttribute
from pynamodb.models import Model

class Card(Model):
    class Meta:
        region = os.environ["AWS_DEFAULT_REGION"]
        table_name = "owllearn-cards"
    deckId = UnicodeAttribute(hash_key=True)
    cardId = UnicodeAttribute(range_key=True)
    front = UnicodeAttribute(default="")
    back = UnicodeAttribute(default="")
    ranking = UnicodeAttribute(default="unranked")

class Deck(Model):
    class Meta:
        region = os.environ["AWS_DEFAULT_REGION"]
        table_name = "owllearn-decks"
    userId = UnicodeAttribute(hash_key=True)
    deckId = UnicodeAttribute(range_key=True)
    cards = MapAttribute(default={}, of=Card)

class DeckPreview(Model):
    class Meta:
        region = os.environ["AWS_DEFAULT_REGION"]
        table_name = "owllearn-deck-previews"
    userId = UnicodeAttribute(hash_key=True)
    deckId = UnicodeAttribute(range_key=True)
    unmarked = NumberAttribute(default=0)
    easy = NumberAttribute(default=0)
    medium = NumberAttribute(default=0)
    hard = NumberAttribute(default=0)