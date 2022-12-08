# Advent of Code 2022, Day 1
# Copyright (c) Benjamin Buzek

from aocd.models import Puzzle
from funcy import print_calls


@print_calls
def part1(input):
    elves = dict()
    elv_total, elv_id = 0, 0
    for cal in input:
        if not cal:
            elves[str(elv_id)] = elv_total
            elv_id += 1
            elv_total = 0
            continue
        elv_total += int(cal)
    return elves[max(elves, key=elves.get)]


@print_calls
def part2(input):
    elves = dict()
    elv_total, elv_id = 0, 0
    for cal in input:
        if not cal:
            elves[str(elv_id)] = elv_total
            elv_id += 1
            elv_total = 0
            continue
        elv_total += int(cal)
    elves = dict(sorted(elves.items(), key=lambda item: item[1], reverse=True)[:3])
    return sum([item[1] for item in elves.items()])


def load(data):
    return data.splitlines()


if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=1)

    sol1 = part1(load(puzzle.input_data))
    assert sol1 == 71780

    sol2 = part2(load(puzzle.input_data))
    assert sol2 == 212489
