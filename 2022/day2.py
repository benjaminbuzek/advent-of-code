# Advent of Code 2022, Day 2
# Copyright (c) Benjamin Buzek

from aocd.models import Puzzle
from funcy import print_calls

P1 = {"A": "Rock", "B": "Paper", "C": "Scissors"}
P2 = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}

LOSE = {"Rock": "Scissors", "Scissors": "Paper", "Paper": "Rock"}
DRAW = {"Rock": "Rock", "Scissors": "Scissors", "Paper": "Paper"}
WIN = {"Rock": "Paper", "Scissors": "Rock", "Paper": "Scissors"}

ACTION_REWARD = {"Rock": 1, "Paper": 2, "Scissors": 3}


@print_calls
def part1(puzzle):
    score = 0
    for play in puzzle:
        action1, action2 = P1[play[0]], P2[play[2]]
        action_reward = ACTION_REWARD[action2]

        if action1 == action2:
            score += (action_reward + 3)

        if action1 == "Rock" and action2 == "Paper":
            score += (action_reward + 6)

        if action1 == "Paper" and action2 == "Rock":
            score += (action_reward + 0)

        if action1 == "Scissors" and action2 == "Rock":
            score += (action_reward + 6)

        if action1 == "Rock" and action2 == "Scissors":
            score += (action_reward + 0)

        if action1 == "Paper" and action2 == "Scissors":
            score += (action_reward + 6)

        if action1 == "Scissors" and action2 == "Paper":
            score += (action_reward + 0)

    return score


@print_calls
def part2(puzzle):
    score = 0
    for play in puzzle:
        action1, action2 = P1[play[0]], P2[play[2]]
        score += action_score(action1, play[2])
    return score


def action_score(action1, decision):
    score = 0
    if decision == "X":
        score = ACTION_REWARD[LOSE[action1]] + 0
    elif decision == "Y":
        score = ACTION_REWARD[DRAW[action1]] + 3
    elif decision == "Z":
        score = ACTION_REWARD[WIN[action1]] + 6
    return score


def split(data):
    return data.split("\n")


if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=2)

    sol1 = part1(split(puzzle.input_data))
    assert sol1 == 11063

    sol2 = part2(split(puzzle.input_data))
    assert sol2 == 10349
