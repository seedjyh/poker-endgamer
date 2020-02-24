#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2020/2/22
import card


class Hand:
    """
    A list of cards that always sorted.
    """
    def __init__(self, cards=None):
        if cards is None:
            cards = []
        self.__cards = cards

    def append_card(self, card):
        self.__cards.append(card)
        self.__sort()

    def __sort(self):
        self.__cards.sort(key=lambda x: x.rank() * 100 + x.suit())

    def __str__(self):
        return "".join(str(x) for x in self.__cards)

    def cards(self):
        return self.__cards

    def first_card(self):
        if len(self.__cards) >= 1:
            return self.__cards[0]
        return None


def fromname(name):
    """
    Initialize an object of Hand from string of name.
    * Name of Hand is list of name of cards in the Hand *
    Raise Exception is name is invalid.
    :param name: list of name, type str, with or without space.
    :return: Object of Hand.
    """
    name = "".join(name.split()).upper()
    if len(name) % 2 != 0:
        raise Exception("length of name must be even")
    hand = Hand()
    for index in range(len(name) // 2):
        hand.append_card(card.fromname(name[index * 2:index * 2+2]))
    return hand


if __name__ == "__main__":
    pass
