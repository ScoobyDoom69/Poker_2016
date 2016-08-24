from pokerdeck import *
from random import choice, shuffle


def deal_hand():
    deck = PokerDeck()
    shuffle(deck)
    myCard = choice(deck)
    hand = []
    for _ in range(5):
        card = choice(deck)
        hand.append(card)
        deck.remove(card)
    return hand

def get_rank(hand):
    rank_list = []
    for card in hand:
        rank_list.append(card.rank)
    return rank_list

def get_suit(hand):
    suit_list = []
    for card in hand:
        suit_list.append(card.suit)
    return suit_list

def royal_flush(ranks, suits):
    flsh = set()
    for suit in suits:
        flsh.add(suit)
    if (ranks.count('A') == 1 and ranks.count('K') == 1 and ranks.count('Q') == 1 and
                ranks.count('J') == 1 and ranks.count('10') == 1 and len(flsh) == 1):
        return True
    else:
        return False

def straight_flush(ranks, suits):
    if royal_flush(ranks, suits) == True:
        return False
    for i in range(len(ranks)):
        if ranks[i] == 'J':
            ranks[i] = '11'
        elif ranks[i] == 'Q':
            ranks[i] = '12'
        elif ranks[i] == 'K':
            ranks[i] = '13'
        if ranks.count('4') > 0:
            if ranks[i] == 'A':
                ranks[i] = '1'
        else:
            if ranks[i] == 'A':
                ranks[i] = '14'
    for i, rank in enumerate(ranks):
        ranks[i] = int(rank)
    ranks.sort()
    flsh = set()
    for suit in suits:
        flsh.add(suit)
    if len(flsh) == 1 and ranks[4] - ranks[0] == 4:
        return True
    else:
        return False

def four_of_a_kind(ranks):
    four_kind = set()
    for rank in ranks:
        if ranks.count(rank) == 4:
            four_kind.add(rank)
    if len(four_kind) == 1:
        return True
    else:
        return False

def full_house(ranks):
    f_h = []
    for rank in ranks:
        if ranks.count(rank) == 2 or ranks.count(rank) == 3:
            f_h.append(rank)
    if len(f_h) == 5:
        return True
    else:
        return False

def flush(ranks, suits):
    if straight_flush(ranks, suits) == True or royal_flush(ranks, suits) == True:
        return False
    flsh = set()
    for suit in suits:
        flsh.add(suit)
    if len(flsh) == 1:
        return True
    else:
        return False

def straight(ranks, suits):
    if straight_flush(ranks, suits) == True or royal_flush(ranks, suits) == True:
        return False
    for i in range(len(ranks)):
        if ranks[i] == 'J':
            ranks[i] = '11'
        elif ranks[i] == 'Q':
            ranks[i] = '12'
        elif ranks[i] == 'K':
            ranks[i] = '13'
        if ranks.count('4') > 0:
            if ranks[i] == 'A':
                ranks[i] = '1'
        else:
            if ranks[i] == 'A':
                ranks[i] = '14'
    for i, rank in enumerate(ranks):
        ranks[i] = int(rank)
    ranks.sort()
    for rank in ranks:
        if ranks.count(rank) > 1:
            return False
    if ranks[4] - ranks[0] == 4:
        return True
    else:
        return False

def three_of_a_kind(ranks):
    if full_house(ranks) == True:
        return False
    th_ki = set()
    for rank in ranks:
        if ranks.count(rank) == 3:
            th_ki.add(rank)
    if len(th_ki) == 1:
        return True
    else:
        return False

def two_pair(ranks):
    pr = set()
    for rank in ranks:
        if ranks.count(rank) == 2:
            pr.add(rank)
    if len(pr) == 2:
        return True
    else:
        return False

def pair(ranks):
    if full_house(ranks) == True:
        return False
    pairs = set()
    for rank in ranks:
        if ranks.count(rank) == 2:
            pairs.add(rank)
    if len(pairs) == 1:
        return True
    else:
        return False

def high_card(ranks, suits):
    if (flush(ranks, suits) == True or straight_flush(ranks, suits) == True or
                straight(ranks, suits) == True or royal_flush(ranks, suits) == True):
        return False
    h_c = set()
    for rank in ranks:
        h_c.add(rank)
    if len(h_c) == 5:
        return True
    else:
        return False

def play_game(ranks, suits):
    if royal_flush(ranks, suits) == True:
        print('You have a royal flush.')
    elif straight_flush(ranks, suits) == True:
        print('You have a straight flush.')
    elif four_of_a_kind(ranks) == True:
        print('You have four of a kind.')
    elif full_house(ranks) == True:
        print('You have a full house.')
    elif flush(ranks, suits) == True:
        print('You have a flush.')
    elif straight(ranks, suits) == True:
        print('You have a straight.')
    elif three_of_a_kind(ranks) == True:
        print('You have three of a kind.')
    elif two_pair(ranks) == True:
        print('You have two pair.')
    elif pair(ranks) == True:
        print('You have a pair.')
    elif high_card(ranks, suits) == True:
        print('You have a high card.')

def main():
    hand = deal_hand()
    hand2 = deal_hand()
    ranks = get_rank(hand)
    ranks2 = get_rank(hand2)
    suits = get_suit(hand)
    suits2 = get_suit(hand2)
    print("Hand 1:")
    [print(r, end=' ') for r in ranks]
    print()
    [print(s, end=' ') for s in suits]
    print()
    play_game(ranks, suits)
    print()
    print()
    print("Hand 2:")
    [print(r, end=' ') for r in ranks2]
    print()
    [print(s, end=' ') for s in suits2]
    print()
    play_game(ranks2, suits2)

if __name__ == '__main__':
    main()