# -*- coding:utf-8 -*-
import time

import hand
from category import identify, Category
from hand import Hand
from normalize import removable_rank, remove_rank, max_removable
from rank import name2rank


class Situation:
    def __init__(self, alice_hand, bob_hand, last_step=None):
        """
        Situation of a game.
        :param alice_hand: Hand of alice. Alice's turn.
        :param bob_hand: Hand of bob
        :param last_step: Hand bob played in the last step. None means bob says "PASS" or it's the beginning of a game.
        """
        if last_step is None:
            last_step = Hand()
        self.__alice_hand = alice_hand
        self.__bob_hand = bob_hand
        self.__last_step = last_step

    def game_over_lost(self):
        return self.__alice_hand.length() > 0 and self.__bob_hand.length() == 0

    def find_playable(self):
        """
        Return a list of hand playable in this situation.
        Notice that if last_step.empty(), None shall not in current list.
        :return: a list of playable hand.
        """
        # PASS
        if self.__last_step.empty():
            for h in self.__alice_hand.select_any():
                yield h
            return
        # None
        yield Hand()
        # Bomb!
        if identify(self.__last_step) is not Category.four_of_a_kind:
            for h in self.__alice_hand.select_four_of_a_kind():
                yield h
        # match category
        if identify(self.__last_step) is Category.individual:
            for h in self.__alice_hand.select_individual():
                if h.first_rank() > self.__last_step.first_rank():
                    yield h
        elif identify(self.__last_step) is Category.pair:
            for h in self.__alice_hand.select_pair():
                if h.first_rank() > self.__last_step.first_rank():
                    yield h
        elif identify(self.__last_step) is Category.three_of_a_kind:
            for h in self.__alice_hand.select_three_of_a_kind():
                if h.first_rank() > self.__last_step.first_rank():
                    yield h
        elif identify(self.__last_step) is Category.four_of_a_kind:
            for h in self.__alice_hand.select_four_of_a_kind():
                if h.first_rank() > self.__last_step.first_rank():
                    yield h
        elif identify(self.__last_step) is Category.straight:
            for h in self.__alice_hand.select_straight_fixed_length(self.__last_step.length()):
                if h.first_rank() > self.__last_step.first_rank():
                    yield h
        else:
            raise Exception("unknown category for last step")

    def play(self, hand):
        """
        Remove cards in hand from alice_hand, and switch alice and bob..
        :param hand:
        :return: nothing
        """
        if hand.empty():  # PASS
            temp_hand = self.__alice_hand.copy()
            self.__alice_hand = self.__bob_hand.copy()
            self.__bob_hand = temp_hand
            self.__last_step = Hand()
        else:
            temp_hand = self.__alice_hand.copy()
            temp_hand.remove(hand)
            self.__alice_hand = self.__bob_hand.copy()
            self.__bob_hand = temp_hand
            self.__last_step = hand.copy()

    def name(self):
        """
        Identify this situation in a single string.
        Suit means nothing here, so use "name" of hand.
        :return:
        """
        return ":".join([h.name() for h in [self.__alice_hand, self.__bob_hand, self.__last_step]])

    def normalize(self):
        """
        "2" shall never decrease (or perhaps a straight appears)
        :return: normalized situation object.
        """
        a_l = self.__alice_hand.ranks()
        b_l = self.__bob_hand.ranks()
        l_l = self.__last_step.ranks()
        now_remove = name2rank("3")
        while now_remove < max_removable(a_l + b_l + l_l):
            if removable_rank(a_l, now_remove) and removable_rank(b_l, now_remove) and removable_rank(l_l, now_remove):
                a_l = remove_rank(a_l, now_remove)
                b_l = remove_rank(b_l, now_remove)
                l_l = remove_rank(l_l, now_remove)
            else:
                now_remove += 1
        return Situation(alice_hand=Hand(ranks=a_l), bob_hand=Hand(ranks=b_l), last_step=Hand(ranks=l_l))

    def copy(self):
        return Situation(alice_hand=self.__alice_hand, bob_hand=self.__bob_hand, last_step=self.__last_step.copy())


def fromname(name):
    alice, bob, last_step = [hand.fromname(n) for n in name.split(":")]
    print(alice, bob, last_step, flush=True)
    return Situation(alice_hand=alice, bob_hand=bob, last_step=last_step)
