from enum import Enum
from dataclasses import dataclass
import random

# suits of the cards
class Suit(Enum):
  HEARTS = 0
  DIAMONDS = 1
  CLUBS = 2
  SPADES = 3

# faces of the cords
class Face(Enum):
    TWO = 1
    THREE = 2
    FOUR = 3
    FIVE = 4
    SIX = 5
    SEVEN = 6
    EIGHT = 7
    NINE = 8
    TEN = 9
    JACK = 10
    QUEEN = 11
    KING = 12
    ACE = 13

# For orginizing and easily accessing the face and suit of cards
@dataclass
class Card:
    face: Face
    suit: Suit

class Deck:
    # function that creates deck of cards by
    # combining the suits and the faces
    def __init__(self):
        self.deck = []
        for face in Face:
            for suit in Suit:
                card = Card(face, suit)
                self.deck.append(card)
        random.shuffle(self.deck)
        # random.shuffle(self.deck)

    def pop_card(self):
        return self.deck.pop()

# function to sort hands by suit, possibly over engineered
def sort_suit(cards):
    hearts, diamonds, spades, clubs = [], [], [], []
    for card in cards:
        match card.suit:
            case Suit.HEARTS:
                hearts.append(card)

            case Suit.CLUBS:
                clubs.append(card)

            case Suit.SPADES:
                spades.append(card)

            case Suit.DIAMONDS:
                diamonds.append(card)

    suits = [hearts, diamonds, spades, clubs]
    sorted_hand = []

    while suits:
        max_suit = max(suits, key=len)

        for card in max_suit:
            sorted_hand.append(card)
        suits.remove(max_suit)

    return sorted_hand

def sort_face(cards):
    sorted_hand = []
    hand_size = len(cards)

    for i in range(hand_size):
        max_card = max(cards, key=lambda x: x.face.value)
        sorted_hand.append(max_card)
        cards.remove(max_card)

    return sorted_hand
