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
    # have the winning 5 card hand be returned along with the win condition
    # revamp check_straight function
    # add functions for full house/two of a kind, royal flush
def check_win(cards):

    fullHouse = False

    cards, pair = check_pair(cards)

    if pair == 4:
        print("Player has four of a kind")
        return True

    if pair == 3:
        cards, fullHouse = check_fh(cards)

    if fullHouse:
        print("Player has a Full House")
        return True

    cards, straight = check_straight(cards)

    if straight:
        print("Player has a straight")
        return True

    cards, flush = check_flush(cards)

    if flush:
        print("Player has a flush")
        return True

    if pair == 3:
        print("Player has a three of a kind")
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
