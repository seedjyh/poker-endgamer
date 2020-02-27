#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2020/2/26

from situation import Situation, fromname


def test_find_playable():
    assert 3 == len([x for x in fromname("345:678:").find_playable()])
    assert 1 == len([x for x in fromname("34567:678:34567").find_playable()])  # pass


def test_fromname():
    assert "345:678:9TJ" == fromname("543:867:TJ9").name()
    assert ":3:" == fromname(":3:").name()


def test_normalize():
    assert fromname("3579:2578:T").normalize().name() == "3457:4562:8"


if __name__ == "__main__":
    pass
