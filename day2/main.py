import re


def deprecated_parse_line(line):
    splitted_line = line.split(":")

    password = splitted_line[1].strip()
    letter = splitted_line[0][-1]
    
    letter_range = splitted_line[0].split(letter)[0].strip()
    letter_range = letter_range.split("-")
    letter_range = [int(number) for number in letter_range]
    
    range_1 = letter_range[0]
    range_2 = letter_range[1]

    return range_1, range_2, letter, password


def parse_line(line : str) -> (int, int, str, str):
    match = re.search('(\d*)-(\d*) (\w): (\w*)', line)
    range_1 = int(match.group(1))
    range_2 = int(match.group(2))
    letter = match.group(3)
    password = match.group(4)

    return range_1, range_2, letter, password


def part_1():
    with open("input.txt", "r") as file:
        lines = file.read().splitlines()
    
    valid_passwords = 0

    for line in lines:
        range_1, range_2, letter, password = parse_line(line)
        count = password.count(letter)

        if count >= range_1 and count <= range_2:
            valid_passwords += 1
    
    print(valid_passwords)


def part_2():
    with open("input.txt", "r") as file:
        lines = file.read().splitlines()
    
    valid_passwords = 0

    for line in lines:
        range_1, range_2, letter, password = parse_line(line)
        if password[range_1 - 1] == letter and password[range_2 - 1] != letter:
            valid_passwords += 1
        elif password[range_1 - 1] != letter and password[range_2 - 1] == letter:
            valid_passwords += 1

    print(valid_passwords)


if __name__ == "__main__":
    part_2()
