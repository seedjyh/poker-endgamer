#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2020/2/26
from hand import fromname
from situation import Situation


def test_find_playable():
    s = Situation(alice_hand=fromname("345"), bob_hand=fromname("678"), last_step=None)
    assert 3 == len([x for x in s.find_playable()])


if __name__ == "__main__":
    pass
