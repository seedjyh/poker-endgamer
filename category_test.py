# -*- coding:utf-8 -*-
from category import identify, beat, Category
import hand


def test_category():
    assert identify(hand.fromname("DA")) is Category.individual
    assert identify(hand.fromname("DA DA")) is Category.pair
    assert identify(hand.fromname("DA SA")) is Category.pair
    assert identify(hand.fromname("DA SA CA")) is Category.three_of_a_kind
    assert identify(hand.fromname("DA SA CA HA")) is Category.four_of_a_kind
    assert identify(hand.fromname("D3 D4 S5 C6 H7")) is Category.straight


def test_beat():
    individual_3 = hand.fromname("S3")
    individual_4 = hand.fromname("S4")
    pair_3 = hand.fromname("S3 D3")
    pair_4 = hand.fromname("S4 D4")
    three_of_a_kind_3 = hand.fromname("S3 D3 H3")
    three_of_a_kind_4 = hand.fromname("S4 D4 H4")
    four_of_a_kind_3 = hand.fromname("S3 D3 H3 C3")
    four_of_a_kind_4 = hand.fromname("S4 D4 H4 C4")
    straight_lowest_5 = hand.fromname("S3 S4 D5 D6 H7")
    straight_lowest_6 = hand.fromname("S3 S4 D5 D6 H7 C8")
    straight_highest_5 = hand.fromname("ST SJ DQ DK CA")
    straight_highest_6 = hand.fromname("S9 ST SJ DQ DK CA")

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
    assert assert_partial_order_beat(individual_3, None)
    assert assert_partial_order_beat(pair_3, None)
    assert assert_partial_order_beat(three_of_a_kind_3, None)
    assert assert_partial_order_beat(four_of_a_kind_3, None)
    assert assert_partial_order_beat(straight_lowest_5, None)
    # Same category, higher beats lower.
    assert assert_partial_order_beat(individual_4, individual_3)
    assert assert_partial_order_beat(pair_4, pair_3)
    assert assert_partial_order_beat(three_of_a_kind_4, three_of_a_kind_3)
    assert assert_partial_order_beat(four_of_a_kind_4, four_of_a_kind_3)
    assert assert_partial_order_beat(straight_highest_5, straight_lowest_5)
    # Different category, four-of-a-kind beats anything.
    assert assert_partial_order_beat(four_of_a_kind_3, individual_4)
    assert assert_partial_order_beat(four_of_a_kind_3, pair_4)
    assert assert_partial_order_beat(four_of_a_kind_3, three_of_a_kind_4)
    assert assert_partial_order_beat(four_of_a_kind_3, straight_highest_5)
    # Different category, not-four-of-a-kind can't beat anything.
    assert not beat(straight_highest_6, straight_lowest_5)
    assert not beat(pair_4, individual_3)
