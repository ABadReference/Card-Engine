from cards.deck52 import *

# this file is for checking win conditions

# function for checking straights
def check_straight(cards):

    # sorts the hand by rank
    cards = sort_face(cards)
    hand = []

    i = 0
    while i < len(cards):

        # # checks if the card face are identicall
        # start = cards[i].face
        if i < len(cards) - 1 and cards[i].face == cards[i+1].face:
            i += 1
            continue

        if i < len(cards) - 1 and cards[i].face.value == cards[i+1].face.value + 1:
            hand.append(cards[i])
            # Once the desired hand size is reached, returns hand and True
            if len(hand) == 5:
                return hand, True

        else:
            hand = []

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

    # if count is 4, returns the winning hand
    if count == 4:

        # adds the 4 of a kind to the hand to be returned
        for card in cards:
            if card.face == face:
                hand.append(card)

        # adds the remaning cards with the highest rank
        for card in cards:
            if card not in hand:
                hand.append(card)

            # returns hand once length is met
            if len(hand) == 5:
                return hand, count

    # if count is not 4 and greater than 1, returns all 7 cards
    elif count > 1:
        # adds the pair to hand first
        for card in cards:
            if card.face == face:
                hand.append(card)

            # breaks once the length of hand is equal to the count
            if len(hand) == count:
                break

        # adds the remaning cards with the highest rank
        for card in cards:
            if card not in hand:
                hand.append(card)

            if len(hand) == len(cards):
                return hand, count

    return cards, 0

# checking for flushes
def check_flush(cards):

    # sorts cards by rank than suit
    cards = sort_face(cards)
    # when sorting by suit, it returns the the suit
    # with the most cards
    cards = sort_suit(cards)

    # returning hand
    hand = []
    # keeps track of suit
    suit = cards[0].suit

    for i in range(len(cards)):
        # returns false once card length - i is less than 5
        if cards[i].suit != suit and len(cards) - i < 5:
           return cards, False
        # card gets appened to hand if suit matches
        if cards[i].suit == suit:
            hand.append(cards[i])
        # returns true once length of hand is 5
        if len(hand) == 5:
            return hand, True

    return cards, False

def check_fh(cards):

    # we are returning hand
    hand = []
    # keeps track of pairs
    count = 0

    # adds pairs from the preorginized list to hand
    for card in cards:
        hand.append(card)
        # breaks once 3 of a kind is added
        if len(hand) == 3:
            break

    # skips the first 3 cards
    i = len(hand)

    while i < len(cards):
        if cards[i] in hand:
            continue
        # if there is a match appends both cards
        if i < len(cards) - 1 and cards[i].face == cards[i+1].face:
            hand.append(cards[i].face)
            hand.append(cards[i+1].face)
            return hand, True
        i += 1

    return cards, False

def check_two_pair(cards):

    # returning hand
    hand = []

    # sort cards by rank searching
    cards = sort_face(cards)

    i = 0

    # loops through each card and searches for pairs
    while i < len(cards):
        # if there is a match appends both cards and increments by two
        if i < len(cards) - 1 and cards[i].face == cards[i+1].face:
            hand.append(cards[i].face)
            hand.append(cards[i+1].face)
            i += 1
        i += 1

    # if hand is not length of 4, we do not have a two pair
    if len(hand) == 4:
        for card in cards:
            # appends the highest ranked card that is not in hand
            if card not in hand:
                hand.append(card)
                return hand, True

    return cards, False
