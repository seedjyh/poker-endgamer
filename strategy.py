#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2020/2/24
from category import beat
from hand import Hand
from select import select_individual, select_straight, select_pair, select_three_of_a_kind, select_four_of_a_kind

class Searcher:
    def __init__(self):
        self.__strategy = dict()  # str(situation-id) -> bool(Winable). No key means not searched.
        # todo: another dict: simpler key for no-straight situation
        # todo: store the dict into a text file.

    def evaluate(self, situation):
        """
        Evaluate the situation. Win-able, or must-lose.
        :param situation:
        :return: True if this situation is win-able.
        """
        if str(situation) in self.__strategy:
            return self.__strategy.get(str(situation))

        # try individual
        all_play = select_individual(situation.alice_hand()) + \
            select_pair(situation.alice_hand()) + \
            select_three_of_a_kind(situation.alice_hand()) + \
            select_four_of_a_kind(situation.alice_hand()) + \
            select_straight(situation.alice_hand())
        for p in all_play:
            if beat(p, situation.last_step()):
                situation.play(p)
                if not self.evaluate(situation):
                    return True
                situation.pullback()
        self.__strategy[str(situation)] = False
        return False


if __name__ == "__main__":
    pass
