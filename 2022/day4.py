# Advent of Code 2022, Day 4
# Copyright (c) Benjamin Buzek

from aocd.models import Puzzle
from funcy import print_calls
import numpy as np


@print_calls
def part1(input):
    count = 0
    for pair in input:
        x, y = np.array(pair, dtype=int)
        if enclosed(x, y):
            count += 1
    return count


@print_calls
def part2(input):
    count = 0
    for pair in input:
        x, y = np.array(pair, dtype=int)
        if overlap(x, y):
            count += 1
    return count


def enclosed(x, y):
    case1 = (x[0] <= y[0] <= x[1] and x[0] <= y[1] <= x[1])
    case2 = (y[0] <= x[0] <= y[1] and y[0] <= x[1] <= y[1])
    if case1 or case2:
        return True
    return False


def overlap(x, y):
    case1 = y[0] <= x[1] and x[0] <= y[1]
    if case1:
        return True
    return False


def split(data):
    a = []
    for x in data.split("\n"):
        a.append([y.split("-") for y in x.split(",")])
    return a


if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=4)

    sol1 = part1(split(puzzle.input_data))
    assert sol1 == 509

    sol2 = part2(split(puzzle.input_data))
    assert sol2 == 870