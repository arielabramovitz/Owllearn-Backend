import os

from pynamodb.attributes import UnicodeAttribute, ListAttribute, NumberAttribute, JSONAttribute
from pynamodb.models import Model

class Card(Model):
    class Meta:
        region = os.environ["AWS_DEFAULT_REGION"]
        table_name = "huji-lightricks-owllearn-cards"
    deckId = UnicodeAttribute(hash_key=True)
    cardId = UnicodeAttribute(range_key=True)
    front = UnicodeAttribute(default="")
    back = UnicodeAttribute(default="")
    ranking = UnicodeAttribute(default="unmarked")

class Deck(Model):
    class Meta:
        region = os.environ["AWS_DEFAULT_REGION"]
        table_name = "huji-lightricks-owllearn-decks"
    userId = UnicodeAttribute(hash_key=True)
    deckId = UnicodeAttribute(range_key=True)
    deckName = UnicodeAttribute(default="")
    cards = ListAttribute(default=[], of=JSONAttribute)
    
    

class DeckPreview(Model):
    class Meta:
        region = os.environ["AWS_DEFAULT_REGION"]
        table_name = "huji-lightricks-owllearn-deck-previews"
    userId = UnicodeAttribute(hash_key=True)
    deckId = UnicodeAttribute(range_key=True)
    deckName = UnicodeAttribute(default="")
    unmarked = NumberAttribute(default=0)
    easy = NumberAttribute(default=0)
    medium = NumberAttribute(default=0)
    hard = NumberAttribute(default=0)
    
    def decrement_rank(self, rank):
        if rank == 'unmarked':
            self.unmarked -= 1
        elif rank == 'easy':
            self.easy -= 1
        elif rank == 'medium':
            self.medium -= 1
        else:
            self.hard -= 1