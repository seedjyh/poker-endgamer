#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2020/2/22


class Hand:
    """
    A list of cards that always sorted.
    """
    def __init__(self):
        self.__cards = []

    def append_card(self, card):
        self.__cards.append(card)
        self.__sort()

    def __sort(self):
        self.__cards.sort(key=lambda x: x.rank() * 100 + x.suit())

    def __str__(self):
        return "".join(str(x) for x in self.__cards)

    def cards(self):
        return self.__cards


if __name__ == "__main__":
    pass
