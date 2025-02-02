from cards.deck52 import *
from winconditions.poker import *

# deals hands for players
def deal_hand(deck):
    hand = []
    i = 0
    num_cards = 2
    while i < num_cards:
        card = deck.pop_card()
        hand.append(card)
        i += 1
    return hand

# first iteration of showing cards aka, The Flop
def flop(deck):
    table = []
    deck.pop_card()
    i = 0
    flop = 3
    while i < flop:
        card = deck.pop_card()
        table.append(card)
        i += 1
    return table

# second and third deal to the table, The Turn and Up the River respectively
def the_turn(deck):
    deck.pop_card()
    return deck.pop_card()

# dedicated function for checking win conditions
# TODO:
    # fix bugs with straight
    # add functions two of a kind, royal flush
def check_win(cards):

    fullHouse = False

#   print("\nCARDS BEFORE CHECKS: ")
    # cards = sort_face(cards)
    # for card in cards: print(card)

    cards, pair = check_pair(cards)
    # cards = sort_face(cards)
    # print("\nCARDS AFTER PAIR: ")
    # for card in cards: print(card)

    if pair == 4:
        # print("Player has four of a kind")
        # for card in cards: print(card)
        return True

    if pair == 3:
        cards, fullHouse = check_fh(cards)
        # cards = sort_face(cards)
        # print("\nCARDS AFTER FULL HOUSE: ")
        # for card in cards: print(card)

    if fullHouse:
        print("Player has a Full House")
        for card in cards: print(card)
        return True

    cards, straight = check_straight(cards)
    # cards = sort_face(cards)
    print("\nCARDS AFTER STRAIGHT: ")
    for card in cards: print(card)

    if straight:
        print("Player has a straight")
        for card in cards: print(card)
        return True

    cards, flush = check_flush(cards)
    # cards = sort_face(cards)
    # print("\nCARDS AFTER FLUSH: ")
    # for card in cards: print(card)

    if flush:
        # print("Player has a flush")
        # for card in cards: print(card)
        return True

    if pair == 3:
        print("Player has a three of a kind")
        # cards = sort_face(cards)
        # for card in cards: print(card)
        return True

    if pair == 2:
        cards, twoPair = check_two_pair(cards)
        if twoPair == True:
            print("Player has two pair")
            return True

        print("Player has a pair")
        return True

if __name__ == "__main__":
    print("Creating a standard 52-card deck...")
    deck = Deck()

    print("\nShuffling the deck...")

    print("\nDealing two hands of cards each...")

    hand1 = deal_hand(deck)
    # hand1 = [Card(Face.NINE, Suit.DIAMONDS)]
    hand2 = deal_hand(deck)

    print("\nHand 1:", hand1)
    print("\nHand 2:", hand2)

    table = flop(deck)

    table.append(the_turn(deck))

    table.append(the_turn(deck))

#   table = [Card(Face.TWO, Suit.HEARTS), Card(Face.FOUR, Suit.DIAMONDS), Card(Face.FIVE,
#             Suit.CLUBS), Card(Face.ACE, Suit.SPADES), Card(Face.THREE, Suit.CLUBS)]

    print("\nThe cards after the river:")
    print(table)

    player1 = check_win(hand1 + table)
    player2 = check_win(hand2 + table)
