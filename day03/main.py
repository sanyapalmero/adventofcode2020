TREE = "#"
RIGHT = 3


def get_data_from_file():
    with open("input.txt", "r") as file:
        lines = file.read().splitlines()
    return lines


def green(symbol):
    return f"\033[92m{symbol}\033[00m"


def red(symbol):
    return f"\033[91m{symbol}\033[00m"


def part_1():
    trees_count = 0
    current_position = RIGHT

    lines = get_data_from_file()
    for line_number, line in enumerate(lines[1:]):
        # for _ in range(6):
        #     line += line
        line = line * 64

        original_len_line = len(line)
        original_line = line

        if len(line) >= current_position and line[current_position] == TREE:
            trees_count += 1
            line = line[:current_position] + green("#") + line[current_position + 1:]
        else:
            line = line[:current_position] + red("0") + line[current_position + 1:]

        # if len(original_line[current_position:]) <= RIGHT:
        #     current_position = RIGHT - len(original_line[current_position:]) - 2
        # if current_position == original_len_line:
        #     current_position = 0

        # print(f"{line_number}\t{line}\t{trees_count}")
        current_position += RIGHT

    print(f"Trees count: {trees_count}")


def part_2():
    trees = []
    ways = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]

    for way in ways:
        current_position = way[0]
        skipping = way[1]
        trees_count = 0
        start = skipping

        lines = get_data_from_file()
        for line in lines[start::skipping]:
            line = line * 80
            # for _ in range(6):
            #     line += line
            # current_position = current_position % len(line)
            if len(line) > current_position and line[current_position] == TREE:
                trees_count += 1

            current_position += way[0]

        trees.append(trees_count)
        print(f"Way: {way}. Trees count: {trees_count}. Rows checked: {len(lines[start::skipping])}.")

    print(trees)
    result = 1
    for tree in trees:
        result *= tree

    print(f"Result: {result}")



def main():
    # part_1()
    part_2()


if __name__ == "__main__":
    main()
