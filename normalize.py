# -*- coding:utf-8 -*-

import rank


def max_removable(ranks):
    """
    max rank in ranks except rank of "2"
    :param ranks:
    :return:
    """
    while rank.name2rank("2") in ranks:
        ranks.remove(rank.name2rank("2"))
    return max(ranks)


def removable_rank(ranks, removed):
    ranks = sorted(ranks)
    if removed in ranks:
        return False
    if len(longest_lower_straight(ranks, removed - 1)) + len(longest_higher_straight(ranks, removed + 1)) >= 5:
        return False
    return True


def longest_lower_straight(ranks, from_rank):
    result = []
    r = from_rank
    while r in ranks:
        result.append(r)
        r -= 1
    result.reverse()
    return result


def longest_higher_straight(ranks, from_rank):
    result = []
    r = from_rank
    while r in ranks and r <= rank.name2rank("A"):
        result.append(r)
        r += 1
    return result


def remove_rank(ranks, removed):
    return [r if r < removed or r > rank.name2rank("A") else r - 1 for r in ranks]
