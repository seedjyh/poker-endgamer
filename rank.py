#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2020/2/22
from enum import Enum


def name2rank(name):
    if len(name) != 1:
        raise Exception("name of rank must be a single letter")
    switch = {
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
        "2": 15,
    }
    if name in switch:
        return switch[name]
    else:
        raise Exception("invalid name of rank, got str: %s" % name)


def rank2name(value):
    return {
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        11: "J",
        12: "Q",
        13: "K",
        14: "A",
        15: "2",
        10: "T",
    }.get(value)


if __name__ == "__main__":
    pass
