#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2020/2/25
import os
import time

import psutil as psutil

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
    # assert evaluate("33556789TJQK2", "6789TJQKAA", "")


def test_searcher_memory_leak():
    t0 = time.clock()
    Searcher().evaluate(Situation(alice_hand=fromname("33556789TJK"), bob_hand=fromname("6789TJQKAA")))
    t1 = time.clock()
    print("33556789TJK: cost=", t1 - t0, flush=True)
    Searcher().evaluate(Situation(alice_hand=fromname("33556789TJ2"), bob_hand=fromname("6789TJQKAA")))
    t2 = time.clock()
    print("33556789TJ2: cost=", t2 - t1, flush=True)


if __name__ == "__main__":
    test_searcher_memory_leak()
