from cards.deck52 import *

# this file is for checking win conditions

# function for checking straights
def check_straight(cards):

    # sorts the hand
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

    # if count is 4, returns the winning hand
    if count == 4:

        # adds the 4 of a kind to the hand to be returned
        for card in cards:
            if card.face == face:
                hand.append(card)

        # adds the remaning cards with the highest rank
        for i in range(len(cards)):
            if face != cards[i].face:
                hand.append(cards[i])

            # returns hand once lenth is met
            if len(hand) == 5:
                return hand, count

            i += 1

    # if count is not 4 and greater than 1, returns all 7 cards
    elif count > 1:
        # adds the pair to hand first
        for card in cards:
            if card.face == face:
                hand.append(card)

            # breaks once the lenth of hand is equal to the count
            if len(hand) == count:
                break

        # adds the remaning cards with the highest rank
        for i in range(len(cards)):
            if face != cards[i].face:
                hand.append(cards[i])

            if len(hand) == len(cards):
                return hand, count

            i += 1

    return cards, 0

# checking for flushes
def check_flush(cards):

    # sorts cards by rank than suit
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

def check_fh(cards):

    # face is made to keep track of what ranks were used
    face = Face
    # we are returning hand
    hand = []
    # keeps track of pairs
    count = 0

    # adds pairs to the preorginized list
    for card in cards:
        hand.append(card)
        # breaks once 3 of a kind is added
        if len(hand) == 3:
            break

    # skips the first 3 cards
    i = 3
    # keeps track of the rank too see if there are any matches
    face = cards[i].face

    # searches the list for a two of a kind
    while i < len(cards) - 1:
        if cards[i].face == face:
            count += 1
        else:
            # resets count to 1 if face mismatch
            count = 1
            # changes the face to new card
            face = cards[i].face
        # breaks once two of a kind is found
        if count == 2:
            break
        i += 1

    # adds the two of a kind to hand and returns it
    for card in cards:
        if card.face == face:
            hand.append(card)
        # returns hand and True once hand has 5 cards
        if len(hand) == 5:
            return hand, True

    return cards, False
