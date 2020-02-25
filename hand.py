#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2020/2/22
import rank
from category import STRAIGHT_MIN_LENGTH


class Hand:
    """
    A list of cards that always sorted.
    """
    def __init__(self, ranks=None):
        if ranks is None:
            ranks = []
        self.__ranks = ranks.copy()
        self.__ranks.sort()

    def append_card(self, card_rank):
        self.__ranks.append(card_rank)
        self.__ranks.sort()

    def __str__(self):
        return "".join(rank.rank2name(x) for x in self.__ranks)

    def ranks(self):
        return self.__ranks.copy()

    def first_rank(self):
        if len(self.__ranks) >= 1:
            return self.__ranks[0]
        return None

    def copy(self):
        return Hand(ranks=self.__ranks.copy())

    def mix(self, hand):
        self.__ranks += hand.__ranks
        self.__ranks.sort()

    def remove(self, hand):
        for r in hand.__ranks:
            self.__ranks.remove(r)

    def id(self):
        """
        Get str made only from rank-name of each cards.
        :return:
        """
        return "".join([rank.rank2name(r) for r in self.__ranks])

    def select_individual(self):
        rank_set = set()
        for r in self.__ranks:
            rank_set.add(r)
        for r in rank_set:
            yield Hand(ranks=[r, ])

    def select_pair(self):
        rank_set = set()
        for r in self.__ranks:
            rank_set.add(r)
        for r in rank_set:
            if self.__ranks.count(r) >= 2:
                yield Hand(ranks=[r, r])

    def select_three_of_a_kind(self):
        rank_set = set()
        for r in self.__ranks:
            rank_set.add(r)
        for r in rank_set:
            if self.__ranks.count(r) >= 3:
                yield Hand(ranks=[r, r, r])

    def select_four_of_a_kind(self):
        rank_set = set()
        for r in self.__ranks:
            rank_set.add(r)
        for r in rank_set:
            if self.__ranks.count(r) >= 4:
                yield Hand(ranks=[r, r, r, r])

    def select_straight(self):
        rank_set = set()
        for r in self.__ranks:
            if rank.name2rank("2") != r:  # "2" can't be used in straight
                rank_set.add(r)
        print(">>>> rank_set:", rank_set)
        now_straight = []
        for r in rank_set:
            if len(now_straight) == 0:
                now_straight.append(r)
            else:
                if now_straight[-1] + 1 == r:
                    now_straight.append(r)
                else:
                    if len(now_straight) >= STRAIGHT_MIN_LENGTH:
                        yield Hand(ranks=now_straight)
                    now_straight = [r, ]
        if len(now_straight) >= STRAIGHT_MIN_LENGTH:
            yield Hand(ranks=now_straight)


def fromname(name):
    """
    Initialize an object of Hand from string of name.
    * Name of Hand is list of name of rank of cards in the Hand *
    Raise Exception is name is invalid.
    :param name: type 'str', name of all ranks with or without space.
    :return: Object of Hand.
    """
    name = "".join(name.split()).upper()
    return Hand(ranks=[rank.name2rank(rn) for rn in name])


if __name__ == "__main__":
    pass
