#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2020/2/22
import rank
import hand
from hand import Hand


def test_hand():
    assert len(Hand().ranks()) == 0
    assert len(Hand(ranks=[rank.name2rank("2"), ]).ranks()) == 1
    assert len(Hand(ranks=[rank.name2rank("2"), rank.name2rank("2"), ]).ranks()) == 2


def test_sort():
    h = Hand()
    h.append_card(rank.name2rank("3"))
    h.append_card(rank.name2rank("3"))
    h.append_card(rank.name2rank("2"))
    assert str(h) == "332"


def test_id():
    assert Hand().id() == ""
    assert hand.fromname("424A3").id() == "344A2"


def test_select_individual():
    result = [x for x in hand.fromname("23A").select_individual()]
    assert len(result) == 3
    assert result[0].first_rank() == rank.name2rank("3")
    assert result[1].first_rank() == rank.name2rank("A")
    assert result[2].first_rank() == rank.name2rank("2")


def test_select_individual_2():
    """
    duplicate rank, different suit
    :return:
    """
    result = [x for x in hand.fromname("22").select_individual()]
    assert len(result) == 1
    assert result[0].first_rank() == rank.name2rank("2")


def test_select_individual_3():
    """
    duplicate rank and suit.
    :return:
    """
    result = [x for x in hand.fromname("22").select_individual()]
    assert len(result) == 1
    assert result[0].first_rank() == rank.name2rank("2")


def test_select_pair():
    result = [x for x in hand.fromname("23").select_pair()]
    assert len(result) == 0


def test_select_pair_2():
    """
    No duplicate pair of the same rank.
    :return:
    """
    result = [x for x in hand.fromname("22222").select_pair()]
    assert len(result) == 1
    assert result[0].first_rank() == rank.name2rank("2")


def test_select_pair_3():
    """
    Order from lower rank to higher.
    :return:
    """
    result = [x for x in hand.fromname("2233AA").select_pair()]
    assert len(result) == 3
    assert result[0].first_rank() == rank.name2rank("3")
    assert result[1].first_rank() == rank.name2rank("A")
    assert result[2].first_rank() == rank.name2rank("2")


def test_select_three_of_a_kind():
    result = [x for x in hand.fromname("2233AA").select_three_of_a_kind()]
    assert len(result) == 0


def test_select_three_of_a_kind_2():
    """
    No duplicate rank in result.
    :return:
    """
    result = [x for x in hand.fromname("2222222222").select_three_of_a_kind()]
    assert len(result) == 1
    assert result[0].first_rank() == rank.name2rank("2")


def test_select_three_of_a_kind_3():
    """
    Order result from lower rank to higher.
    :return:
    """
    result = [x for x in hand.fromname("222333").select_three_of_a_kind()]
    assert len(result) == 2
    assert result[0].first_rank() == rank.name2rank("3")
    assert result[1].first_rank() == rank.name2rank("2")


def test_select_four_of_a_kind():
    result = [x for x in hand.fromname("222333").select_four_of_a_kind()]
    assert len(result) == 0


def test_select_four_of_a_kind_2():
    result = [x for x in hand.fromname("2222").select_four_of_a_kind()]
    assert len(result) == 1
    assert result[0].first_rank() == rank.name2rank("2")


def test_select_four_of_a_kind_3():
    """
    Ordered result from lower rank to higher rank.
    :return:
    """
    result = [x for x in hand.fromname("22223333").select_four_of_a_kind()]
    assert len(result) == 2
    assert result[0].first_rank() == rank.name2rank("3")
    assert result[1].first_rank() == rank.name2rank("2")


def test_select_straight_separated():
    result = [x for x in hand.fromname("22223333").select_straight_separated()]
    assert len(result) == 0


def test_select_straight_separated_2():
    """
    As long as possible.
    :return:
    """
    result = [x for x in hand.fromname("3456789TJQKA2").select_straight_separated()]
    assert len(result) == 1
    assert len(result[0].ranks()) == len("3456789TJQKA")


def test_select_straight_separated_3():
    """
    No duplicate range.
    :return:
    """
    result = [x for x in hand.fromname("345678934567").select_straight_separated()]
    assert len(result) == 1
    assert len(result[0].ranks()) == len("3456789")
    assert result[0].first_rank() == rank.name2rank("3")


def test_select_straight_separated_4():
    """
    Order from lower rank to higher rank.
    :return:
    """
    result = [x for x in hand.fromname("345678TJQKA2").select_straight_separated()]
    assert len(result) == 2
    assert len(result[0].ranks()) == len("345678")
    assert result[0].first_rank() == rank.name2rank("3")
    assert len(result[1].ranks()) == len("TJQKA")
    assert result[1].first_rank() == rank.name2rank("T")


def test_select_straight_fixed_length():
    result = [x for x in hand.fromname("3456789T").select_straight_fixed_length(6)]
    assert len(result) == 3
    assert result[0].id() == "345678"
    assert result[1].id() == "456789"
    assert result[2].id() == "56789T"


def test_select_straight_any_length():
    result = [x for x in hand.fromname("3456789T").select_straight_any_length()]
    assert len(result) == 4 + 3 + 2 + 1
    assert result[0].id() == "34567"
    assert result[1].id() == "45678"
    assert result[2].id() == "56789"
    assert result[3].id() == "6789T"
    assert result[4].id() == "345678"
    assert result[5].id() == "456789"
    assert result[6].id() == "56789T"
    assert result[7].id() == "3456789"
    assert result[8].id() == "456789T"
    assert result[9].id() == "3456789T"


if __name__ == "__main__":
    pass
