import time
from contextlib import contextmanager


EMPTY_SEAT = "L"
OCCUPIED_SEAT = "#"
FLOOR = "."


def get_matrix():
    with open("input.txt") as file:
        rows = file.read().splitlines()

    matrix = []
    for row in rows:
        matrix.append(list(row))

    return matrix


def display_matrix(matrix):
    for row in matrix:
        print("".join(row))


def get_adjacent_places(row: int, column: int, matrix):
    up = (row - 1, column)
    down = (row + 1, column)
    left = (row, column - 1)
    right = (row, column + 1)
    diagonal_up_left = (row - 1, column - 1)
    diagonal_up_right = (row - 1, column + 1)
    diagonal_down_left = (row + 1, column - 1)
    diagonal_down_right = (row + 1, column + 1)

    positions = [
        up,
        down,
        left,
        right,
        diagonal_up_left,
        diagonal_up_right,
        diagonal_down_left,
        diagonal_down_right,
    ]

    adjacent_places = []
    for position in positions:
        row_idx, column_idx = position
        if row_idx < 0 or column_idx < 0:
            continue
        elif row_idx > len(matrix[0]) - 1 or column_idx > len(matrix[0]) - 1:
            continue
        
        adjacent_places.append(matrix[row_idx][column_idx])

    return adjacent_places


def part_1():
    matrix = get_matrix()
    rows, columns = len(matrix), len(matrix[0])

    iteration = 0
    chaos = True
    while chaos:
        new_matrix = []
        rows_changes = []
        for row in range(rows):
            row_changed = False
            new_row = []
            for column in range(columns):
                place = matrix[row][column]
                adjacent_places = get_adjacent_places(row, column, matrix)
                if place == EMPTY_SEAT and OCCUPIED_SEAT not in adjacent_places:
                    new_row.append(OCCUPIED_SEAT)
                    row_changed = True
                elif place == OCCUPIED_SEAT and adjacent_places.count(OCCUPIED_SEAT) >= 4:
                    new_row.append(EMPTY_SEAT)
                    row_changed = True
                else:
                    new_row.append(place)
            new_matrix.append(new_row)
            rows_changes.append(row_changed)
        
        # print(f"Iteration: {iteration}. Matrix:")
        # display_matrix(new_matrix)
        # print("--------------------------------")

        if True not in rows_changes:
            chaos = False

        iteration += 1
        matrix.clear()
        matrix = new_matrix
    
    occupied_count = 0
    for row in matrix:
        for seat in row:
            if seat == OCCUPIED_SEAT:
                occupied_count += 1
    print(f"Occupied count: {occupied_count}. Iterations: {iteration}")


def get_directions(row: int, column: int, matrix):
    max_row_idx = len(matrix[0])

    directions = []
    directions.append([(row - i, column) for i in range(1, max_row_idx)]) # up
    directions.append([(row + i, column) for i in range(1, max_row_idx)]) # down
    directions.append([(row, column - i) for i in range(1, max_row_idx)]) # left
    directions.append([(row, column + i) for i in range(1, max_row_idx)]) # right
    directions.append([(row - i, column - i) for i in range(1, max_row_idx)]) # diagonal_up_left
    directions.append([(row - i, column + i) for i in range(1, max_row_idx)]) # diagonal_up_right
    directions.append([(row + i, column - i) for i in range(1, max_row_idx)]) # diagonal_down_left
    directions.append([(row + i, column + i) for i in range(1, max_row_idx)]) # diagonal_down_right

    directions_list = []
    for direction in directions:
        temp_direction = []
        for position in direction:
            row_idx, column_idx = position
            if row_idx < 0 or column_idx < 0:
                continue
            elif row_idx > len(matrix[0]) - 1 or column_idx > len(matrix[0]) - 1:
                continue
            
            temp_direction.append(matrix[row_idx][column_idx])
        directions_list.append(temp_direction)

    return directions_list


def part_2():
    matrix = get_matrix()
    rows, columns = len(matrix), len(matrix[0])

    iteration = 0
    chaos = True
    while chaos:
        new_matrix = []
        rows_changes = []
        for row in range(rows):
            row_changed = False
            new_row = []
            for column in range(columns):
                place = matrix[row][column]
                directions = get_directions(row, column, matrix)
                first_elements = []
                for direction in directions:
                    for element in direction:
                        if element == FLOOR:
                            continue
                        else:
                            first_elements.append(element)
                            break

                if place == EMPTY_SEAT and OCCUPIED_SEAT not in first_elements:
                    new_row.append(OCCUPIED_SEAT)
                    row_changed = True
                elif place == OCCUPIED_SEAT and first_elements.count(OCCUPIED_SEAT) >= 5:
                    new_row.append(EMPTY_SEAT)
                    row_changed = True
                else:
                    new_row.append(place)
            new_matrix.append(new_row)
            rows_changes.append(row_changed)
        
        # print(f"Iteration: {iteration}. Matrix:")
        # display_matrix(new_matrix)
        # print("--------------------------------")

        if True not in rows_changes:
            chaos = False

        iteration += 1
        matrix.clear()
        matrix = new_matrix
    
    occupied_count = 0
    for row in matrix:
        for seat in row:
            if seat == OCCUPIED_SEAT:
                occupied_count += 1
    print(f"Occupied count: {occupied_count}. Iterations: {iteration}")


@contextmanager
def timeit():
    time_start = time.time()
    yield
    elapsed = time.time() - time_start
    print(f"[took {elapsed * 1000:0.2f}ms]")


if __name__ == "__main__":
    part_1()
    with timeit():
        part_2()