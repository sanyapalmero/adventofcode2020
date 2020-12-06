from functools import reduce
from operator import __and__


def read_file():
    with open("input.txt") as file:
        lines = file.read().splitlines()
        lines.append(None)
        return lines


def part_1():
    yes_count = 0
    lines = read_file()
    
    questions = set()
    for line in lines:
        if line:
            questions.update(line)  
        else:
            yes_count += len(questions)
            questions = set()

    print(yes_count)


def part_2():
    yes_count = 0
    lines = read_file()

    questions = []
    for line in lines:
        if line:
            questions.append(set(line))
        else:
            yes_count += len(list(reduce(__and__, questions)))
            questions = []

    print(yes_count)


if __name__ == "__main__":
    part_1()
    part_2()
