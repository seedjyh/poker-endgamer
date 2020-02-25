#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2020/2/24
from category import beat


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
        if situation.id() in self.__strategy:
            return self.__strategy.get(situation.id())

        if situation.game_over_lost():
            self.store_evaluate_result(situation, False)
            return False

        for h in situation.find_playable():
            now_situation = situation.copy()
            now_situation.play(h)
            if not self.evaluate(now_situation):
                self.store_evaluate_result(situation, True)
                return True
        self.store_evaluate_result(situation, False)
        return False

    def store_evaluate_result(self, situation, result):
        self.__strategy[situation.id()] = result
        print(">>> store", situation.id(), "as", result, "total", len(self.__strategy))


if __name__ == "__main__":
    pass
