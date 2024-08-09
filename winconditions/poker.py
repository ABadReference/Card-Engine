from cards.deck52 import *

# this file is for checking win conditions

# function for checking straights
def check_straight(cards):

    cards = sort_face(cards)
    hand = []

    i = 0
    while i < len(cards):

        # Once the desired hand size is reached, returns hand and True
        if len(hand) == 5:
            return hand, True

        # checks if the card face are identicall
        start = cards[i].face
        if i < len(cards) - 1 and start == cards[i+1].face:
            i += 1
            continue

        # resets the deck if the values do not match
        if i < len(cards) - 1 and start.value - 1 != cards[i+1].face.value:
            hand = []

        hand.append(cards[i])

        i += 1

    return cards, False

# functions for checking pairs
def check_pair(cards):

    # sorts cards by rank
    cards = sort_face(cards)

    # has an array size of 13 to easily count the ammount of pairs
    faces_count = [0] * 13

    # initials values:
        # count: for keeping track of pair count
        # face: keeps track of the face of pairs
        # hand: return value
    count = 1
    face = Face
    hand = []

    # matches the value of the face to the location of the array
    for card in cards:
        faces_count[card.face.value-1] += 1

        # checks to see what face card has the highest count
        if faces_count[card.face.value-1] > count:
            face = card.face
            count = faces_count[card.face.value-1]

    # if count is less then 2, returns false
    if count >= 2:

        # adds the pair in hand to be returned
        for card in cards:
            if card.face == face:
                hand.append(card)

        # adds the remaning cards with the highest rank
        for i in range(len(cards)):
            if face != cards[i].face:
                hand.append(cards[i])
            if len(hand) == 5:
                return hand, count
            i += 1

    return cards, False

# checking for flushes
def check_flush(cards):

    cards = sort_face(cards)
    cards = sort_suit(cards)

    hand = []
    suit = cards[0].suit

    for card in cards:
        if card.suit == suit:
            hand.append(card)
        if len(hand) == 5:
            return hand, True

    return cards, False
