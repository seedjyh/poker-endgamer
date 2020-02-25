# -*- coding:utf-8 -*-
from category import identify, beat, Category
import hand


def test_category():
    assert identify(hand.fromname("A")) is Category.individual
    assert identify(hand.fromname("AA")) is Category.pair
    assert identify(hand.fromname("AA")) is Category.pair
    assert identify(hand.fromname("AAA")) is Category.three_of_a_kind
    assert identify(hand.fromname("AAAA")) is Category.four_of_a_kind
    assert identify(hand.fromname("34567")) is Category.straight


def test_beat():
    individual_3 = hand.fromname("3")
    individual_4 = hand.fromname("4")
    pair_3 = hand.fromname("33")
    pair_4 = hand.fromname("44")
    three_of_a_kind_3 = hand.fromname("333")
    three_of_a_kind_4 = hand.fromname("444")
    four_of_a_kind_3 = hand.fromname("3333")
    four_of_a_kind_4 = hand.fromname("4444")
    straight_lowest_5 = hand.fromname("34567")
    straight_lowest_6 = hand.fromname("345678")
    straight_highest_5 = hand.fromname("TJQKA")
    straight_highest_6 = hand.fromname("9TJQKA")

    def assert_partial_order_beat(hand_a, hand_b):
        """
        "Beat" is partial order(if A beats B, then B can't beat A).
        :param hand_a:
        :param hand_b:
        :return:
        """
        assert beat(hand_a, hand_b)
        assert not beat(hand_b, hand_a)

    # Anything beats none (opposite says "PASS")
    assert_partial_order_beat(individual_3, None)
    assert_partial_order_beat(pair_3, None)
    assert_partial_order_beat(three_of_a_kind_3, None)
    assert_partial_order_beat(four_of_a_kind_3, None)
    assert_partial_order_beat(straight_lowest_5, None)
    # Same category, higher beats lower.
    assert_partial_order_beat(individual_4, individual_3)
    assert_partial_order_beat(pair_4, pair_3)
    assert_partial_order_beat(three_of_a_kind_4, three_of_a_kind_3)
    assert_partial_order_beat(four_of_a_kind_4, four_of_a_kind_3)
    assert_partial_order_beat(straight_highest_5, straight_lowest_5)
    # Different category, four-of-a-kind beats anything.
    assert_partial_order_beat(four_of_a_kind_3, individual_4)
    assert_partial_order_beat(four_of_a_kind_3, pair_4)
    assert_partial_order_beat(four_of_a_kind_3, three_of_a_kind_4)
    assert_partial_order_beat(four_of_a_kind_3, straight_highest_5)
    # Different category, not-four-of-a-kind can't beat anything.
    assert not beat(straight_highest_6, straight_lowest_5)
    assert not beat(pair_4, individual_3)
