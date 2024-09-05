from cards.deck52 import *
from winconditions.poker import *

# deals hands for players
def deal_hand(deck, num_cards=2):
    hand = []
    for i in range(num_cards):
        card = deck.pop_card()
        hand.append(card)
    return hand

# first iteration of showing cards aka, The Flop
def flop(deck):
    table = []
    deck.pop_card()
    for i in range(3):
        card = deck.pop_card()
        table.append(card)
    return table

# second and third deal to the table, The Turn and Up the River respectively
def the_turn(deck):
    deck.pop_card()
    return deck.pop_card()

# dedicated function for checking win conditions
# TODO:
    # fix bugs with flush and full house
    # add functions two of a kind, royal flush
def check_win(cards):

    fullHouse = False

    print("\nCARDS BEFORE CHECKS: ")
    # cards = sort_face(cards)
    for card in cards: print(card)

    cards, pair = check_pair(cards)
    # cards = sort_face(cards)
    print("\nCARDS AFTER PAIR: ")
    for card in cards: print(card)

    if pair == 4:
        print("Player has four of a kind")
        for card in cards: print(card)
        return True

    if pair == 3:
        cards, fullHouse = check_fh(cards)
        # cards = sort_face(cards)
        print("\nCARDS AFTER FULL HOUSE: ")
        for card in cards: print(card)

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
    print("\nCARDS AFTER FLUSH: ")
    for card in cards: print(card)

    if flush:
        print("Player has a flush")
        for card in cards: print(card)
        return True

    if pair == 3:
        print("Player has a three of a kind")
        # cards = sort_face(cards)
        for card in cards: print(card)
        return True

    if pair == 2:
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

    # table = [Card(Face.TEN, Suit.HEARTS), Card(Face.NINE, Suit.DIAMONDS), Card(Face.NINE,
    #         Suit.CLUBS), Card(Face.TEN, Suit.SPADES), Card(Face.TEN, Suit.CLUBS)]

    print("\nThe cards after the river:")
    print(table)

    player1 = check_win(hand1 + table)
    player2 = check_win(hand2 + table)
