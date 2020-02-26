# -*- coding:utf-8 -*-
import hand
from category import identify, Category
from hand import Hand


class Situation:
    def __init__(self, alice_hand, bob_hand, last_step=None):
        """
        Situation of a game.
        :param alice_hand: Hand of alice. Alice's turn.
        :param bob_hand: Hand of bob
        :param last_step: Hand bob played in the last step. None means bob says "PASS" or it's the beginning of a game.
        """
        self.__alice_hand = alice_hand
        self.__bob_hand = bob_hand
        self.__last_step = last_step

    def game_over_lost(self):
        return self.__alice_hand.length() > 0 and self.__bob_hand.length() == 0

    def find_playable(self):
        """
        Return a list of hand playable in this situation.
        Notice that if last_step is None, None shall not in current list.
        :return: a list of playable hand.
        """
        # PASS
        if self.__last_step is None:
            for h in self.__alice_hand.select_any():
                yield h
            return
        # None
        yield None
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
                yield h
        else:
            raise Exception("unknown category for last step")

    def play(self, hand):
        """
        Remove cards in hand from alice_hand, and switch alice and bob..
        :param hand:
        :return: nothing
        """
        if hand is None:  # PASS
            temp_hand = self.__alice_hand.copy()
            self.__alice_hand = self.__bob_hand.copy()
            self.__bob_hand = temp_hand
            self.__last_step = None
        else:
            temp_hand = self.__alice_hand.copy()
            temp_hand.remove(hand)
            self.__alice_hand = self.__bob_hand.copy()
            self.__bob_hand = temp_hand
            self.__last_step = hand.copy()

    def pullback(self):
        """
        Append cards into bob_hand, and switch alice and bob.
        :return: nothing
        """
        prev_alice = self.__bob_hand.copy().append(self.__last_step)
        prev_bob = self.__alice_hand.copy()
        self.__alice_hand = prev_alice
        self.__bob_hand = prev_bob

    def name(self):
        """
        Identify this situation in a single string.
        Suit means nothing here, so use "name" of hand.
        :return:
        """
        alice_name = self.__alice_hand.name()
        bob_name = self.__bob_hand.name()
        last_step_name = ""
        if self.__last_step is not None:
            last_step_name = self.__last_step.name()
        return ":".join([alice_name, bob_name, last_step_name])

    def compressed_name(self):
        return self.__alice_hand.name()

    def copy(self):
        last_step = None
        if self.__last_step is not None:
            last_step = self.__last_step.copy()
        return Situation(alice_hand=self.__alice_hand, bob_hand=self.__bob_hand, last_step=last_step)


def fromname(name):
    alice, bob, last_step = [hand.fromname(n) for n in name.split(":")]
    return Situation(alice_hand=alice, bob_hand=bob, last_step=last_step)
