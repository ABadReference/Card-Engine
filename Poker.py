from cards.deck import *

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
    # fix this for the future
def check_win(cards):
    # cards = sort_suit(cards)
    # print("Sorted by suit:")
    # cards = sort_face(cards)
    # print("\n\nSorted by face:")
    print(cards)
    hand, flush = check_flush(cards)

    pair = check_pair(cards)

    straight = check_straight(cards)

    if straight:
        print("Player has a straight")
        return True

    if flush:
        print("Player has a flush")
        return True

    if pair == 4:
        print("Player has four of a kind")
        return True

    if pair == 3:
        print("Player has a three of a kind")
        return True

    if pair == 2:
        print("Player has a pair")
        return True

def check_straight(cards):
    faces_count = [0] * 13
    count = 0
    for card in cards:
        faces_count[card.face.value-1] += 1

    for face in faces_count:
        if face == 0:
            count = 0
        else:
            count += 1
            if count >= 5:
                return True

    return False

def check_pair(cards):
    faces_count = [0] * 13
    for card in cards:
        faces_count[card.face.value-1] += 1
    total_pairs = max(faces_count)

    return total_pairs if total_pairs >= 2 else 0

# checking for flushes
def check_flush(cards):

    cards = sort_face(cards)
    cards = sort_suit(cards)
    print(f"Cards should be sorted by suit:\n\n{cards}")

    hand = []

    suit = cards[0].suit

    for card in cards:
        if card.suit == suit:
            hand.append(card)
        if len(hand) == 5:
            print(hand)
            return hand, True

    return None, False


if __name__ == "__main__":
    print("Creating a standard 52-card deck...")
    deck = Deck()

    print("\nShuffling the deck...")

    print("\nDealing two hands of cards each...")

    hand1 = deal_hand(deck)
    hand2 = deal_hand(deck)

    print("\nHand 1:", hand1)
    print("\nHand 2:", hand2)

    table = flop(deck)

    table.append(the_turn(deck))

    table.append(the_turn(deck))

    # table = [Card(Face.NINE, Suit.CLUBS), Card(Face.THREE, Suit.CLUBS), Card(Face.FOUR,
    #         Suit.CLUBS), Card(Face.TEN, Suit.CLUBS), Card(Face.SEVEN, Suit.CLUBS)]

    print("\nThe cards after the river:")
    print(table)

    player1 = check_win(hand1 + table)
    # player2 = check_win(hand2 + table)
