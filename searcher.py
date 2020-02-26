#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2020/2/24


from knowledge import SituationValuation


class Searcher:
    def __init__(self):
        self.__knowledge = SituationValuation()

    def evaluate(self, situation):
        """
        Evaluate the situation. Win-able, or must-lose.
        :param situation:
        :return: True if this situation is win-able.
        """
        v = self.__knowledge.query(situation)
        if v is not None:
            return v

        if situation.game_over_lost():
            self.__knowledge.save(situation, False)
            return False

        for h in situation.find_playable():
            now_situation = situation.copy()
            now_situation.play(h)
            if not self.evaluate(now_situation):
                self.__knowledge.save(situation, True)
                return True
        self.__knowledge.save(situation, False)
        return False


if __name__ == "__main__":
    pass
