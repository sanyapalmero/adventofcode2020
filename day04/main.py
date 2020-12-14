import json
import re

REQUIRED_FIELDS_COUNT = 8
OPTIONAL_FIELD = "cid"


def get_data_from_file():
    with open("input.txt", "r") as file:
        lines = file.read().splitlines()
    return lines


def is_passport_valid(passport):
    filled_keys = len(list(passport.keys()))
    if filled_keys == REQUIRED_FIELDS_COUNT:
        return True
    elif filled_keys == REQUIRED_FIELDS_COUNT - 1 and OPTIONAL_FIELD not in passport.keys():
        return True
    else:
        # invalid_passport = json.dumps(passport, indent=4)
        # print(f"Invalid passport: {invalid_passport}")
        return False


def part_1():
    lines = get_data_from_file()

    passports = []
    temp_passport = {}

    for line in lines:
        if line:
            splitted_line = line.split(" ")
            for data in splitted_line:
                key, value = data.split(":")
                temp_passport[key] = value
        else:
            passports.append(temp_passport)
            temp_passport = {}
    passports.append(temp_passport)

    valid_passports = 0
    invalid_passwords = 0
    for passport in passports:
        # print(json.dumps(passport, indent=4))
        if is_passport_valid(passport):
            valid_passports += 1
        else:
            invalid_passwords += 1

    print(f"Passports count: {len(passports)}. Valid: {valid_passports}. Invalid: {invalid_passwords}")


def is_passport_good_filled(passport):
    stats = []
    for key, value in passport.items():
        if key == "byr":
            if len(value) == 4 and int(value) >= 1920 and int(value) <= 2002:
                stats.append(True)
            else:
                stats.append(False)

        if key == "iyr":
            if len(value) == 4 and int(value) >= 2010 and int(value) <= 2020:
                stats.append(True)
            else:
                stats.append(False)

        if key == "eyr":
            if len(value) == 4 and int(value) >= 2020 and int(value) <= 2030:
                stats.append(True)
            else:
                stats.append(False)

        if key == "hgt":
            if "cm" in value:
                if int(value[:-2]) >= 150 and int(value[:-2]) <= 193:
                    stats.append(True)
                else:
                    stats.append(False)
            elif "in" in value:
                if int(value[:-2]) >= 59 and int(value[:-2]) <= 76:
                    stats.append(True)
                else:
                    stats.append(False)
            else:
                stats.append(False)

        if key == "hcl":
            # if re.match("#[0-9][0-9][0-9][a-f][a-f][a-f]", value) is not None:
            # if re.fullmatch("(#)([0-9]|[a-f])([0-9]|[a-f])([0-9]|[a-f])([0-9]|[a-f])([0-9]|[a-f])([0-9]|[a-f])", value) is not None:
            if re.match(r"^#[0-9a-f]{6}$", value):
                stats.append(True)
            else:
                stats.append(False)

        if key == "ecl":
            if value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                stats.append(True)
            else:
                stats.append(False)

        if key == "pid":
            # if re.match("00000000[0-9]", value) is not None:
            # if len(value) == 9 and "0" in value:
            # if len(value) == 9:
            if re.match(r"^\d{9}$", value):
                stats.append(True)
            else:
                stats.append(False)

        if key == "cid":
            stats.append(True)

    if False in stats:
        # print(stats, passport)
        return False
    else:
        return True

    # return False if False in stats else True

def part_2():
    lines = get_data_from_file()

    passports = []
    temp_passport = {}

    for line in lines:
        if line:
            splitted_line = line.split(" ")
            for data in splitted_line:
                key, value = data.split(":")
                temp_passport[key] = value
        else:
            passports.append(temp_passport)
            temp_passport = {}
    passports.append(temp_passport)

    valid_passports = 0
    invalid_passwords = 0
    for passport in passports:
        if is_passport_valid(passport) and is_passport_good_filled(passport):
            valid_passports += 1
        else:
            invalid_passwords += 1

    print(f"Passports count: {len(passports)}. Valid: {valid_passports}. Invalid: {invalid_passwords}")


def main():
    # part_1()
    part_2()


if __name__ == "__main__":
    main()
