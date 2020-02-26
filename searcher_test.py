#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2020/2/25

import time
from hand import fromname
from searcher import Searcher
from situation import Situation

s = Searcher()


def evaluate(alice, bob, last):
    return s.evaluate(Situation(alice_hand=fromname(alice), bob_hand=fromname(bob), last_step=fromname(last)))


def test_searcher():
    assert not evaluate("35", "46", "")
    assert evaluate("36", "45", "")
    assert evaluate("45678", "4", "")
    assert not evaluate("45678", "4", "2")
    assert evaluate("45678", "4", "34567")
    assert evaluate("334455", "2", "")
    assert not evaluate("33445567", "2", "")
    assert not evaluate("33556789TJK", "6789TJQKAA", "")
    assert not evaluate("33556789TJ2", "6789TJQKAA", "")
    # assert evaluate("33556789TJQK2", "6789TJQKAA", "")


if __name__ == "__main__":
    pass
