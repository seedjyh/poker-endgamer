#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2020/2/22
from card import fromname, Suit


def test_card():
    # name to value
    assert fromname("SJ").suit() == Suit.spade
    assert fromname("HQ").suit() == Suit.heart
    assert fromname("DK").suit() == Suit.diamond
    assert fromname("CA").suit() == Suit.club
    assert fromname("S2").rank() == 15
    # name to value and to name
    for n in ["SA", "H2", "D3", "C4", "S5", "H6", "D7", "C8", "S9", "HT", "DJ", "CQ", "SK"]:
        assert fromname(n).name() == n


if __name__ == "__main__":
    pass

