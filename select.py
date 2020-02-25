#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2020/2/23
from card import Card, rank2name, name2rank
from hand import Hand


def same_rank(*args):
    for index in range(len(args)):
        if args[index].rank() != args[0].rank():
            return False
    return True


def select_individual(hand):
    """
    Find all kind of individual Hand in current hand.
    :param hand: current hand, object of Hand.
    :return: a list of hand in category of individual. The order would be from increasing rank.
    """
    last_rank = None
    for card in hand.cards():
        if card.rank() != last_rank:
            last_rank = card.rank()
            yield Hand(cards=[card, ])


def select_pair(hand):
    last_rank = None
    cards = hand.cards()
    for index in range(len(cards)):
        if index >= 1 and same_rank(cards[index], cards[index-1]) and cards[index].rank() != last_rank:
            last_rank = cards[index].rank()
            yield Hand(cards=cards[index-1:index+1])


def select_three_of_a_kind(hand):
    last_rank = None
    cards = hand.cards()
    for index in range(len(cards)):
        if index >= 2 and same_rank(cards[index], cards[index-1],  cards[index-2]) and cards[index].rank() != last_rank:
            last_rank = cards[index].rank()
            yield Hand(cards=cards[index-2:index+1])


def select_four_of_a_kind(hand):
    last_rank = None
    cards = hand.cards()
    for index in range(len(cards)):
        if index >= 3 and same_rank(cards[index], cards[index-1],  cards[index-2],  cards[index-3]) and\
                cards[index].rank() != last_rank:
            last_rank = cards[index].rank()
            yield Hand(cards=cards[index-3:index+1])


STRAIGHT_MIN_LENGTH = 5


def select_straight(hand):
    rank_set = set()
    for card in hand.cards():
        rank_set.add(card.rank())
    for s in get_largest_successive_rank_sets(rank_set):
        if name2rank("2") in s:
            s.remove(name2rank("2"))
        if len(s) >= STRAIGHT_MIN_LENGTH:
            yield select_hand_by_rank_set(hand, s)


def get_largest_successive_rank_sets(rank_set):
    """
    Separate original set into a list of set, in which items successive to each other.
    Each set returned should be as large as possible.

    {3,4,5,7,8,9,11} => [{3,4,5}, {7,8,9}, {11,}]

    :param rank_set: set of rank.
    :return: list of set of rank.
    """
    now_set = set()
    for rank in rank_set:
        if len(now_set) == 0:
            now_set.add(rank)
        else:
            if max(now_set) + 1 == rank:
                now_set.add(rank)
            else:
                yield now_set
                now_set = {rank}
    if len(now_set) > 0:
        yield now_set


def select_hand_by_rank_set(hand, rank_set):
    left_set = rank_set.copy()
    result = Hand()
    for card in hand.cards():
        if card.rank() in left_set:
            result.append_card(card)
            left_set.remove(card.rank())
    if len(left_set) == 0:
        return result
    else:
        raise Exception("no expected rank named:" + rank2name(max(left_set)))


if __name__ == "__main__":
    pass
