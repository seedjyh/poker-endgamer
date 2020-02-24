# -*- coding:utf-8 -*-
import category
import hand


def test_is_pair():
    assert category.is_pair(hand.fromname("DADA"))


def test_is_straight():
    assert category.is_straight(hand.fromname("D3 D4 S5 C6 H7"))


def test_category():
    assert category.identify(hand.fromname("DA")) is category.Category.individual
    assert category.identify(hand.fromname("DA DA")) is category.Category.pair
    assert category.identify(hand.fromname("DA SA")) is category.Category.pair
    assert category.identify(hand.fromname("DA SA CA")) is category.Category.three_of_a_kind
    assert category.identify(hand.fromname("DA SA CA HA")) is category.Category.four_of_a_kind
    assert category.identify(hand.fromname("D3 D4 S5 C6 H7")) is category.Category.straight
