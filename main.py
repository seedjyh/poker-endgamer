#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2020/2/27

import sys
import searcher
import situation


def get_result(game_situation):
    return searcher.Searcher().evaluate(game_situation)


def search_next_step(game_situation):
    for step in game_situation.find_playable():
        gs = game_situation.copy()
        gs.play(step)
        if not get_result(gs):
            print("now:", game_situation.name(), "play:", step.name(), "result:", gs.name())
            return step.name()
    return None


if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) == 3 and sys.argv[1] == "win":
        if get_result(situation.fromname(sys.argv[2])):
            print("Yes, you win!")
        else:
            print("No, you will lose.")
    elif len(sys.argv) == 3 and sys.argv[1] == "next":
        next_step = search_next_step(situation.fromname(sys.argv[2]))
        if next_step is not None:
            print("You should play:", next_step)
        else:
            print("No way, you will definitely lose.")
    else:
        print("unknown command")
