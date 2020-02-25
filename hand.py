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
        self.__cardnames = [c.name() for c in cards]

    def append_card(self, new_card):
        self.__cardnames.append(new_card.name())
        self.__sort()

    def __sort(self):
        self.__cardnames.sort(key=lambda cn: card.fromname(cn).weight())

    def __str__(self):
        return "".join(str(x) for x in self.__cardnames)

    def cards(self):
        return [card.fromname(cn) for cn in self.__cardnames]

    def first_card(self):
        if len(self.__cardnames) >= 1:
            return card.fromname(self.__cardnames[0])
        return None

    def copy(self):
        return Hand(cards=self.cards().copy())

    def mix(self, hand):
        self.__cardnames += hand.__cardnames
        self.__sort()

    def remove(self, hand):
        for cn in hand.__cardnames:
            self.__cardnames.remove(cn)

    def id(self):
        """
        Get str made only from rank-name of each cards.
        :return:
        """
        return "".join([card.fromname(cn).rank_name() for cn in self.__cardnames])


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
