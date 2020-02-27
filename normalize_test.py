# -*- coding:utf-8 -*-
from normalize import longest_lower_straight, longest_higher_straight, removable_rank, remove_rank


def test_longest_lower_straight():
    assert longest_lower_straight([3, 4, 6, 7], 8) == []
    assert longest_lower_straight([3, 4, 6, 7], 7) == [6, 7]
    assert longest_lower_straight([3, 4, 6, 6, 7, 7], 7) == [6, 7]


def test_longest_higher_straight():
    assert [] == longest_higher_straight([9, 10, 12, 13, 14, 15], 8)
    assert longest_higher_straight([9, 10, 12, 13, 14, 15], 9) == [9, 10, ]
    assert longest_higher_straight([9, 9, 10, 12, 13, 14, 15], 9) == [9, 10, ]
    assert longest_higher_straight([9, 10, 12, 13, 14, 15], 12) == [12, 13, 14, ]  # no "2"


def test_removable_rank():
    assert not removable_rank([3, 4, 5], 3)
    assert removable_rank([4, 5], 3)
    assert not removable_rank([9, 10, 12, 13, 14, 15, ], 11)
    assert removable_rank([10, 12, 13, 14, 15, ], 11)  # "2" will not be pull down
    assert removable_rank([3, 4, 5, 7], 9)
    assert removable_rank([4, 5, 6, 15], 9)
    assert removable_rank([8, ], 9)


def test_remove_rank():
    assert remove_rank([4, 5, 6], 3) == [3, 4, 5]
    assert remove_rank([10, 11, 13, 14, 15], 12) == [10, 11, 12, 13, 15]
