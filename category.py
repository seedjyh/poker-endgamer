#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2020/2/23
from enum import Enum


class Category(Enum):
    individual = 1
    pair = 2
    three_of_a_kind = 3
    four_of_a_kind = 4
    straight = 5


def identify(hand):
    """
    Identify the category of Hand.
    :param hand: object of Hand
    :return: value of enum Category. None means no valid category
    """
    work = {
        is_individual: Category.individual,
        is_pair: Category.pair,
        is_three_of_a_kind: Category.three_of_a_kind,
        is_four_of_a_kind: Category.four_of_a_kind,
        is_straight: Category.straight,
    }
    for k, v in work.items():
        if k(hand):
            return v
    else:
        return None


def is_individual(hand):
    return len(hand.cards()) == 1


def is_pair(hand):
    cards = hand.cards()
    return len(cards) == 2 and cards[0].rank() == cards[1].rank()


def is_three_of_a_kind(hand):
    cards = hand.cards()
    return len(cards) == 3 and cards[0].rank() == cards[-1].rank()


def is_four_of_a_kind(hand):
    cards = hand.cards()
    return len(cards) == 4 and cards[0].rank() == cards[-1].rank()


def is_straight(hand):
    cards = hand.cards()
    if len(cards) < 5:
        return False
    for index in range(len(cards)):
        if index > 1 and cards[index-1].rank() + 1 != cards[index].rank():
            return False
    return True


def beat(new_hand, last_hand):
    """
    Check is new_hand could beat the last_hand
    :param new_hand:
    :param last_hand:
    :return: True if new_hand could beat last_hand.
    """
    new_category = identify(new_hand)
    if new_category is None:
        return False
    last_category = identify(last_hand)
    if last_category is None:
        raise True
    if new_category != last_category:
        return new_category == Category.four_of_a_kind
    if new_category in [Category.individual, Category.pair, Category.three_of_a_kind, Category.four_of_a_kind]:
        return new_hand.first_card().rank() > last_hand.first_card().rank()
    if new_category is Category.straight:
        return len(new_hand.cards()) == len(last_hand.cards()) and \
               new_hand.first_card().rank() > last_hand.first_card().rank()
    

if __name__ == "__main__":
    pass
