INPUT_FILE = "input.txt"
TEST_FILE = "test.txt"

TEST_MODE = False

FRONT_SEAT = "F"
BACK_SEAT = "B"
LEFT_SEAT = "L"
RIGHT_SEAT = "R"


def read_file():
    file_name = TEST_FILE if TEST_MODE else INPUT_FILE
    with open(file_name) as file:
        return file.read().splitlines()


def part_1():
    lines = read_file()
    ids = []
    for line in lines:
        rows_range = [i for i in range(128)]
        columns_range = [i for i in range(8)]

        for symbol in line:
            if symbol == FRONT_SEAT:
                rows_range = rows_range[:int(len(rows_range) / 2)]
            elif symbol == BACK_SEAT:
                rows_range = rows_range[int(len(rows_range) / 2):]

            if symbol == LEFT_SEAT:
                columns_range = columns_range[:int(len(columns_range) / 2)]
            elif symbol == RIGHT_SEAT:
                columns_range = columns_range[int(len(columns_range) / 2):]

        row = rows_range[0]
        column = columns_range[0]
        line_id = (row * 8) + column
        ids.append(line_id)
        # print(f"{line}, row: {row}, column: {column}, id: {line_id}")
    print(f"Max id: {max(ids)}")


def part_2():
    lines = read_file()
    ids = []
    for line in lines:
        rows_range = [i for i in range(128)]
        columns_range = [i for i in range(8)]

        for symbol in line:
            if symbol == FRONT_SEAT:
                rows_range = rows_range[:int(len(rows_range) / 2)]
            elif symbol == BACK_SEAT:
                rows_range = rows_range[int(len(rows_range) / 2):]

            if symbol == LEFT_SEAT:
                columns_range = columns_range[:int(len(columns_range) / 2)]
            elif symbol == RIGHT_SEAT:
                columns_range = columns_range[int(len(columns_range) / 2):]

        row = rows_range[0]
        column = columns_range[0]
        line_id = (row * 8) + column
        ids.append(line_id)
        # print(f"{line}, row: {row}, column: {column}, id: {line_id}")

    for id in range(min(ids), max(ids)):
        if id not in ids:
            print(f"My id: {id}")



if __name__ == "__main__":
    # part_1()
    part_2()
