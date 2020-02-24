#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2020/2/24
from enum import Enum


class Player(Enum):
    alice = 1
    bob = 2


class Situation:
    def __init__(self, alice_hand, bob_hand, now_turn=Player.alice, last_step=None):
        """
        Situation of a game.
        :param alice_hand: Hand of alice
        :param bob_hand: Hand of bob
        :param now_turn: current player
        :param last_step: the opponent player played in the last step
        """
        self.__alice_hand = alice_hand
        self.__bob_hand = bob_hand
        self.__now_turn = now_turn
        self.__last_step = last_step

    def alice_hand(self):
        return self.__alice_hand

    def bob_hand(self):
        return self.__bob_hand

    def now_turn(self):
        return self.__now_turn

    def last_step(self):
        return self.__last_step


def search(situation):
    """
    Find the choice for play in this turn to win this situation.
    :param situation:
    :return: Hand to play in this turn to win this game. None means no way to win.
    """
    return None


if __name__ == "__main__":
    pass
