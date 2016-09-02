from Poker_Summer2016 import *
from pokerdeck import *

def test_deal_hand():
    assert(len(deal_hand()) == 5)

def test_no_dupes():
    hand = deal_hand()
    for card in hand:
        assert hand.count(card) == 1

def test_get_rank():
    ranks_hand = [Card(rank='4', suit='♥'), Card(rank='K', suit='♣'), Card(rank='A', suit='♦'),
                  Card(rank='2', suit='♠'), Card(rank='9', suit='♠')]
    assert get_rank(ranks_hand) == ['4', 'K', 'A', '2', '9']

def test_get_suit():
    suits_hand = [Card(rank='4', suit='♥'), Card(rank='K', suit='♣'), Card(rank='A', suit='♦'),
                  Card(rank='2', suit='♠'), Card(rank='9', suit='♠')]
    assert get_suit(suits_hand) == ['♥','♣','♦','♠','♠']

def test_high_card():
    flush_hand = [Card(rank='4', suit='♥'), Card(rank='K', suit='♥'), Card(rank='A', suit='♥'),
                  Card(rank='2', suit='♥'), Card(rank='9', suit='♥')]
    straight_flush_hand = [Card(rank='4', suit='♥'), Card(rank='3', suit='♥'), Card(rank='A', suit='♥'),
                  Card(rank='2', suit='♥'), Card(rank='5', suit='♥')]
    straight_hand = [Card(rank='4', suit='♥'), Card(rank='3', suit='♣'), Card(rank='A', suit='♦'),
                  Card(rank='2', suit='♠'), Card(rank='5', suit='♠')]
    royal_flush_hand = [Card(rank='Q', suit='♥'), Card(rank='K', suit='♥'), Card(rank='A', suit='♥'),
                  Card(rank='J', suit='♥'), Card(rank='10', suit='♥')]
    pair_hand = [Card(rank='Q', suit='♥'), Card(rank='Q', suit='♥'), Card(rank='A', suit='♥'),
                  Card(rank='J', suit='♥'), Card(rank='10', suit='♥')]
    high_card_hand = [Card(rank='4', suit='♥'), Card(rank='K', suit='♣'), Card(rank='A', suit='♦'),
                  Card(rank='2', suit='♠'), Card(rank='9', suit='♠')]
    assert high_card(get_rank(flush_hand), get_suit(flush_hand)) == False
    assert high_card(get_rank(straight_flush_hand), get_suit(straight_flush_hand)) == False
    assert high_card(get_rank(straight_hand), get_suit(straight_hand)) == False
    assert high_card(get_rank(royal_flush_hand), get_suit(royal_flush_hand)) == False
    assert high_card(get_rank(pair_hand), get_suit(pair_hand)) == False
    assert high_card(get_rank(high_card_hand), get_suit(high_card_hand)) == True

def test_pair():
    pair_hand = ['9','9','A','Q','J']
    no_pair_hand = ['8','9','A','Q','J']
    f_h_hand = ['9','9','A','A','A']
    assert pair(pair_hand) == True
    assert pair(no_pair_hand) == False
    assert pair(f_h_hand) == False

def test_two_pair():
    two_pair_hand = ['9','9','A','A','J']
    not_two_pair = ['9','9','A','Q','J']
    assert two_pair(two_pair_hand) == True
    assert two_pair(not_two_pair) == False

def test_three_of_a_kind():
    three_kind_hand = ['9','9','9','A','J']
    not_three_kind = ['9','8','10','A','J']
    f_h_hand = ['9','9','A','A','A']
    assert three_of_a_kind(three_kind_hand) == True
    assert three_of_a_kind(not_three_kind) == False
    assert three_of_a_kind(f_h_hand) == False

def test_straight():
    straight_flush_hand = [Card(rank='4', suit='♥'), Card(rank='3', suit='♥'), Card(rank='A', suit='♥'),
                  Card(rank='2', suit='♥'), Card(rank='5', suit='♥')]
    royal_flush_hand = [Card(rank='Q', suit='♥'), Card(rank='K', suit='♥'), Card(rank='A', suit='♥'),
                  Card(rank='J', suit='♥'), Card(rank='10', suit='♥')]
    not_straight_hand = [Card(rank='4', suit='♥'), Card(rank='K', suit='♣'), Card(rank='A', suit='♦'),
                  Card(rank='2', suit='♠'), Card(rank='9', suit='♠')]
    straight_hand1 =  [Card(rank='4', suit='♥'), Card(rank='3', suit='♣'), Card(rank='A', suit='♦'),
                  Card(rank='2', suit='♠'), Card(rank='5', suit='♠')]
    straight_hand2 = [Card(rank='J', suit='♥'), Card(rank='Q', suit='♣'), Card(rank='K', suit='♦'),
                  Card(rank='10', suit='♠'), Card(rank='9', suit='♠')]
    assert straight(get_rank(straight_flush_hand), get_suit(straight_flush_hand)) == False
    assert straight(get_rank(royal_flush_hand), get_suit(royal_flush_hand)) == False
    assert straight(get_rank(not_straight_hand), get_suit(not_straight_hand)) == False
    assert straight(get_rank(straight_hand1), get_suit(straight_hand1)) == True
    assert straight(get_rank(straight_hand2), get_suit(straight_hand2)) == True

def test_flush():
    flush_hand = ['♠','♠','♠','♠','♠']
    not_flush_hand = ['♥','♣','♦','♠','♠']
    ranks_in_hand = ['2','5','7','6','9']
    assert flush(ranks_in_hand, flush_hand) == True
    assert flush(ranks_in_hand, not_flush_hand) == False

def test_full_house():
    f_h_hand = ['9','9','A','A','A']
    not_f_h_hand = ['9','10','J','4','A']
    assert full_house(f_h_hand) == True
    assert full_house(not_f_h_hand) == False

def test_alphas():
    ranks = ['J', 'Q', 'K', 'A']
    for i in range(len(ranks)):
        if ranks[i] == 'J':
            ranks[i] = '11'
        elif ranks[i] == 'Q':
            ranks[i] = '12'
        elif ranks[i] == 'K':
            ranks[i] = '13'
        elif ranks[i] == 'A':
            ranks[i] = '1'
    assert ranks.count('11') == 1
    assert ranks.count('12') == 1
    assert ranks.count('13') == 1
    assert ranks.count('1') == 1