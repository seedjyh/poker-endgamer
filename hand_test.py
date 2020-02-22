#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2020/2/22
import card
from hand import Hand


def test_sort():
    hand = Hand()
    hand.append_card(card.fromname("S3"))
    hand.append_card(card.fromname("D3"))
    hand.append_card(card.fromname("S2"))
    assert str(hand) == "S3D3S2"
    hand.sort()
    assert str(hand) == "D3S3S2"


if __name__ == "__main__":
    pass
