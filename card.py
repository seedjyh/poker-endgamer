#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2020/2/22
from enum import Enum


class Suit:
    spade = 4
    heart = 3
    diamond = 2
    club = 1


def name2suit(name):
    return {
        "S": Suit.spade,
        "H": Suit.heart,
        "D": Suit.diamond,
        "C": Suit.club,
    }.get(name)


def suit2name(value):
    return {
        Suit.spade: "S",
        Suit.heart: "H",
        Suit.diamond: "D",
        Suit.club: "C",
    }.get(value)


def name2rank(name):
    return {
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
    }.get(name)


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


class Card:
    def __init__(self, suit, rank):
        self.__suit = suit
        self.__rank = rank

    def suit(self):
        return self.__suit

    def rank(self):
        return self.__rank

    def name(self):
        return suit2name(self.__suit) + rank2name(self.__rank)

    def __str__(self):
        return self.name()


def fromname(name):
    if len(name) != 2:
        raise Exception("invalid name for this card")
    return Card(suit=name2suit(name[0]), rank=name2rank(name[1]))


if __name__ == "__main__":
    pass
