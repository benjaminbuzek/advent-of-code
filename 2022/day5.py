# Advent of Code 2022, Day 5
# Copyright (c) Benjamin Buzek

from aocd.models import Puzzle
from funcy import print_calls


@print_calls
def part1(actions, state, stacks, indexes):
    loadStacks(state, stacks, indexes)
    for instruction in actions:
        instruction = instruction.replace("move", "").replace("from ", "").replace("to ", "").strip().split(" ")
        instruction = [int(i) for i in instruction]

        crates = instruction[0]
        from_stack = instruction[1]
        to_stack = instruction[2]

        for crate in range(crates):
            crate_removed = stacks[from_stack].pop()
            stacks[to_stack].append(crate_removed)

    return getStackEnds(stacks)


@print_calls
def part2(actions, state, stacks, indexes):
    emptyStacks(stacks)
    loadStacks(state, stacks, indexes)
    for instruction in actions:
        instruction = instruction.replace("move", "").replace("from ", "").replace("to ", "").strip().split(" ")
        instruction = [int(i) for i in instruction]

        crates = instruction[0]
        from_stack = instruction[1]
        to_stack = instruction[2]

        crates_to_remove = stacks[from_stack][-crates:]
        stacks[from_stack] = stacks[from_stack][:-crates]

        for crate in crates_to_remove:
            stacks[to_stack].append(crate)

    return getStackEnds(stacks)


def loadStacks(state, stacks, indexes):
    for string in state[:-1]:
        stack_num = 1
        for index in indexes:
            if string[index] == " ":
                pass
            else:
                stacks[stack_num].insert(0, string[index])
            stack_num += 1


def emptyStacks(stacks):
    for stack_num in stacks:
        stacks[stack_num].clear()


def getStackEnds(stacks):
    answer = ""
    for stack in stacks:
        answer += stacks[stack][-1]
    return answer


def split(input):
    state, actions = (i.splitlines() for i in input.strip('\n').split('\n\n'))
    return state, actions


if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=5)

    stack_string, instructions = split(puzzle.input_data)
    stacks = {int(digit): [] for digit in stack_string[-1].replace(" ", "")}
    indexes = [index for index, char in enumerate(stack_string[-1]) if char != " "]

    sol1 = part1(instructions, stack_string, stacks, indexes)
    assert sol1 == 'DHBJQJCCW'

    sol2 = part2(instructions, stack_string, stacks, indexes)
    assert sol2 == 'WJVRLSJJT'
