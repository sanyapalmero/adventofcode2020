def read_file():
    with open("input.txt") as f:
        return f.read().splitlines()


INPUT_PREAMBLE_LENGTH = 25
TEST_PREAMBLE_LENGTH = 5


def is_valid_number(number, preamble):
    for num_1 in preamble:
        for num_2 in preamble:
            if num_1 + num_2 == number:
                return True
    return False


def part_1():
    numbers = read_file()
    numbers = list(map(int, numbers))
    preamble_length = INPUT_PREAMBLE_LENGTH
    preamble = numbers[:preamble_length]
    skipped_preamble_list = numbers[preamble_length:]
    
    for number in skipped_preamble_list:
        if is_valid_number(number, preamble):
            preamble.pop(0)
            preamble.append(number)
        else:
            print(number)
            break


def search_list(numbers, not_valid_number):
    searched_numbers = []
    sum_numbers = 0
    while sum_numbers <= not_valid_number:
        for number in numbers:
            searched_numbers.append(number)
            sum_numbers += number
            if sum_numbers == not_valid_number:
                return searched_numbers
            elif sum_numbers > not_valid_number:
                sum_numbers = 0
                searched_numbers.clear()
                break
        numbers.pop(0)


def part_2():
    numbers = read_file()
    numbers = list(map(int, numbers))
    preamble_length = INPUT_PREAMBLE_LENGTH
    preamble = numbers[:preamble_length]
    skipped_preamble_list = numbers[preamble_length:]
    
    not_valid_number = None
    for number in skipped_preamble_list:
        if is_valid_number(number, preamble):
            preamble.pop(0)
            preamble.append(number)
        else:
            not_valid_number = number
            break
    
    searched_numbers = search_list(numbers, not_valid_number)    
    print(min(searched_numbers) + max(searched_numbers))


if __name__ == "__main__":
    part_1()
    part_2()
