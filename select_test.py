# -*- coding:utf-8 -*-
from card import name2rank
import hand
from select import select_individual, select_pair, select_three_of_a_kind, select_four_of_a_kind, select_straight


def test_select_individual():
    result = [x for x in select_individual(hand.fromname("D2D3DA"))]
    assert len(result) == 3
    assert result[0].first_card().rank() == name2rank("3")
    assert result[1].first_card().rank() == name2rank("A")
    assert result[2].first_card().rank() == name2rank("2")


def test_select_individual_2():
    """
    duplicate rank, different suit
    :return:
    """
    result = [x for x in select_individual(hand.fromname("D2S2"))]
    assert len(result) == 1
    assert result[0].first_card().rank() == name2rank("2")


def test_select_individual_3():
    """
    duplicate rank and suit.
    :return:
    """
    result = [x for x in select_individual(hand.fromname("D2D2"))]
    assert len(result) == 1
    assert result[0].first_card().rank() == name2rank("2")


def test_select_pair():
    result = [x for x in select_pair(hand.fromname("S2D3"))]
    assert len(result) == 0


def test_select_pair_2():
    """
    No duplicate pair of the same rank.
    :return:
    """
    result = [x for x in select_pair(hand.fromname("S2S2H2C2C2"))]
    assert len(result) == 1
    print(">>>>>", result[0].cards())
    print(">>>>>", result[0].first_card())
    assert result[0].first_card().rank() == name2rank("2")


def test_select_pair_3():
    """
    Order from lower rank to higher.
    :return:
    """
    result = [x for x in select_pair(hand.fromname("S2S2S3C3DADA"))]
    assert len(result) == 3
    assert result[0].first_card().rank() == name2rank("3")
    assert result[1].first_card().rank() == name2rank("A")
    assert result[2].first_card().rank() == name2rank("2")


def test_select_three_of_a_kind():
    result = [x for x in select_three_of_a_kind(hand.fromname("S2S2S3C3DADA"))]
    assert len(result) == 0


def test_select_three_of_a_kind_2():
    """
    No duplicate rank in result.
    :return:
    """
    result = [x for x in select_three_of_a_kind(hand.fromname("S2S2S2D2H2S2S2S2D2H2"))]
    assert len(result) == 1
    assert result[0].first_card().rank() == name2rank("2")


def test_select_three_of_a_kind_3():
    """
    Order result from lower rank to higher.
    :return:
    """
    result = [x for x in select_three_of_a_kind(hand.fromname("S2S2S2D3D3D3"))]
    assert len(result) == 2
    assert result[0].first_card().rank() == name2rank("3")
    assert result[1].first_card().rank() == name2rank("2")


def test_select_four_of_a_kind():
    result = [x for x in select_four_of_a_kind(hand.fromname("S2S2S2D3D3D3"))]
    assert len(result) == 0


def test_select_four_of_a_kind_2():
    result = [x for x in select_four_of_a_kind(hand.fromname("S2S2S2D2"))]
    assert len(result) == 1
    assert result[0].first_card().rank() == name2rank("2")


def test_select_four_of_a_kind_3():
    """
    Ordered result from lower rank to higher rank.
    :return:
    """
    result = [x for x in select_four_of_a_kind(hand.fromname("S2S2S2S2D3D3D3D3"))]
    assert len(result) == 2
    assert result[0].first_card().rank() == name2rank("3")
    assert result[1].first_card().rank() == name2rank("2")


def test_select_straight():
    result = [x for x in select_straight(hand.fromname("S2S2S2S2D3D3D3D3"))]
    assert len(result) == 0


def test_select_straight_2():
    """
    As long as possible.
    :return:
    """
    result = [x for x in select_straight(hand.fromname("S3S4S5S6S7S8S9 ST SJ SQ SK SA S2"))]
    assert len(result) == 1
    assert len(result[0].cards()) == len("3456789TJQKA")


def test_select_straight_3():
    """
    No duplicate range.
    :return:
    """
    result = [x for x in select_straight(hand.fromname("S3S4S5S6S7S8S9D3D4D5D6D7"))]
    assert len(result) == 1
    assert len(result[0].cards()) == len("3456789")
    assert result[0].first_card().rank() == name2rank("3")


def test_select_straight_4():
    """
    Order from lower rank to higher rank.
    :return:
    """
    result = [x for x in select_straight(hand.fromname("S3S4S5S6S7S8 DT DJ DQ DK DA H2"))]
    assert len(result) == 2
    assert len(result[0].cards()) == len("345678")
    assert result[0].first_card().rank() == name2rank("3")
    assert len(result[1].cards()) == len("TJQKA")
    assert result[1].first_card().rank() == name2rank("T")
