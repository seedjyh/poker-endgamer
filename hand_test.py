#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2020/2/22
import card
import hand
from hand import Hand


def test_hand():
    assert len(Hand().cards()) == 0
    assert len(Hand(cards=[card.fromname("D2"), ]).cards()) == 1
    assert len(Hand(cards=[card.fromname("D2"), card.fromname("D2"), ]).cards()) == 2


def test_sort():
    hand = Hand()
    hand.append_card(card.fromname("S3"))
    hand.append_card(card.fromname("D3"))
    hand.append_card(card.fromname("S2"))
    assert str(hand) == "D3S3S2"


def test_id():
    assert Hand().id() == ""
    assert hand.fromname("S4H2C4SAD3").id() == "344A2"


if __name__ == "__main__":
    pass
