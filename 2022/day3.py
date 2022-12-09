# Advent of Code 2022, Day 3
# Copyright (c) Benjamin Buzek

from aocd.models import Puzzle
from funcy import print_calls
import string

alphabet = list(string.ascii_lowercase)
ALPHABET = list(string.ascii_uppercase)


@print_calls
def part1(input):
    item_sum = 0
    for item in backpacks(input):
        shared_item = list(set(item[0]).intersection(item[1]))[0]
        if shared_item.islower():
            index = alphabet.index(shared_item) + 1
        else:
            index = ALPHABET.index(shared_item) + 27
        item_sum += index
    return item_sum


@print_calls
def part2(input):
    item_sum = 0
    for item in groups(input):
        shared_item = list(set.intersection(set(item[0]), set(item[1]), set(item[2])))[0]
        if shared_item.islower():
            index = alphabet.index(shared_item) + 1
        else:
            index = ALPHABET.index(shared_item) + 27
        item_sum += index
    return item_sum


def backpacks(input):
    backpack = []
    for compartment in input:
        a = slice(0, len(compartment) // 2)
        b = slice(len(compartment) // 2, len(compartment))
        backpack.append([compartment[a], compartment[b]])
    return backpack


def groups(input):
    group, groups = [], []
    for item_id, item in enumerate(input):
        group.append(item)
        if (item_id + 1) % 3 == 0:
            groups.append(group)
            group = []
    return groups


def split(input):
    return input.split("\n")


if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=3)

    sol1 = part1(split(puzzle.input_data))
    assert sol1 == 7428

    sol2 = part2(split(puzzle.input_data))
    assert sol2 == 2650
