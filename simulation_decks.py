# Simulation decks
import random
import collections

DECKS = ['spades', 'hearts', 'diamonds', 'clubs']
VALUES = [i for i in range(1,14)]

def create_deck():
    """This function create a deck"""
    decks = []
    for deck in DECKS:
        for value in VALUES:
            decks.append((deck, value))
    return decks

def get_hand(decks, len_hand):
    """Obtain a random hand"""
    hand = random.sample(decks, len_hand)

    return hand

def checkConsecutive(l):
    """Check if is a straight"""
    return sorted(l) == list(range(min(l), max(l)+1)) 

def main(len_hand, times):
    """get the probabilities of the hands"""
    decks = create_deck()

    hands = []
    for _ in range(times):
        hand = get_hand(decks, len_hand)
        hands.append(hand)
    
    pairs = 0
    three_of_a_kind = 0
    straight = 0
    for hand in hands:
        values = [card[1] for card in hand]
        counter = dict(collections.Counter(values))
        for val in counter.values():
            if val == 2:
                pairs += 1
                break
            elif val == 3:
                three_of_a_kind += 1
                break
        if checkConsecutive(values):
            straight += 1

    pair_probability = pairs / times
    print(f'The probability of get a pair in one hand of {len_hand} cards is {pair_probability}')
    
    three_probability = three_of_a_kind / times
    print(f'The probability of get a three of a kind in one hand of {len_hand} cards is {three_probability}')

    straight_probability = straight / times
    print(f'The probability of get a straight in one hand of {len_hand} cards is {straight_probability}')

if __name__ == '__main__':
    try:
        len_hand = int(input('How many cards will the hand have? '))
        times = int(input("how many times do you want to run the simulation? "))

        main(len_hand, times)
    except KeyboardInterrupt as ki:
        print("\n This process has been canceled. Retry.")
    
    