from cards.deck import *

# this file is for checking win conditions

# function for checking straights
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
