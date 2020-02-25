#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2020/2/22
from rank import name2rank, rank2name


def test_card():
    # name to value
    assert name2rank("2") == 15
    # name to value and to name
    for n in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]:
        assert rank2name(name2rank(n)) == n


if __name__ == "__main__":
    pass

