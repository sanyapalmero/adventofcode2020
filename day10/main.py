BUILTIN_JOLTAGE_ADAPTER_DIFFERENCE = 3


def get_joltage_ratings_list():
    with open("input.txt") as file:
        joltage_list = [int(joltage.strip()) for joltage in file.readlines()]
        return joltage_list


def part_1():
    joltage_list = get_joltage_ratings_list()
    builtin_joltage_adapter = max(joltage_list) + BUILTIN_JOLTAGE_ADAPTER_DIFFERENCE
    
    difference_of_1 = []
    difference_of_3 = []

    jolt = 0
    while jolt <= builtin_joltage_adapter:
        available_jolts = [i + jolt for i in range(1, 4)]
        founded_jolts = []
        for available_jolt in available_jolts:
            if available_jolt in joltage_list:
                founded_jolts.append(available_jolt)
        if len(founded_jolts) == 1 and founded_jolts[0] - jolt == 3:
            difference_of_3.append(founded_jolts[0])
            jolt = founded_jolts[0]
        elif len(founded_jolts) >= 1 and min(founded_jolts) - jolt == 1:
            difference_of_1.append(min(founded_jolts))
            jolt = min(founded_jolts)
        elif jolt + BUILTIN_JOLTAGE_ADAPTER_DIFFERENCE == builtin_joltage_adapter:
            difference_of_3.append(jolt)
            break
        else:
            jolt += 1

    print(f"Count of difference 1: {len(difference_of_1)}")
    print(f"Count of difference 3: {len(difference_of_3)}")
    print(f"Final result: {len(difference_of_1) * len(difference_of_3)}")


# From description of the part 2: "there must be more than a trillion valid ways to arrange them!"
# Now this is an avengers level threat!
def part_2():
    joltage_list = get_joltage_ratings_list()
    builtin_joltage_adapter = max(joltage_list) + BUILTIN_JOLTAGE_ADAPTER_DIFFERENCE

    # Solution from https://dev.to/qviper/advent-of-code-2020-python-solution-day-10-30kd
    sol = {0: 1}
    for line in sorted(joltage_list):
        sol[line] = 0
        if line - 1 in sol.keys():
            sol[line] += sol[line - 1]
        if line - 2 in sol.keys():
            sol[line] += sol[line - 2]
        if line - 3 in sol.keys():
            sol[line] += sol[line - 3]

    print(sol[max(joltage_list)])
    
    # Solution from https://www.reddit.com/r/adventofcode/comments/ka8z8x/2020_day_10_solutions/gfdfthy?utm_source=share&utm_medium=web2x&context=3
    last_jolt = max(joltage_list)
    # index = [1] + [0] * last_jolt + [0, 0]
    idxs = [0 for _ in range(builtin_joltage_adapter)] # Create list of zeros length as builtin_joltage_adapter
    idxs[0] = 1 # Replace first element from 0 to 1, because 0 always first element and it's count always 1
    for jolt in sorted(joltage_list): # Loop by sorted jolts from file 
        idxs[jolt] = idxs[jolt - 1] + idxs[jolt - 2] + idxs[jolt - 3] # Sum values of -1, -2, -3 indexes of current jolt
        if jolt == last_jolt:
            print(idxs[jolt])
            break

    # Solution from https://www.reddit.com/r/adventofcode/comments/ka8z8x/2020_day_10_solutions/gfdinh7?utm_source=share&utm_medium=web2x&context=3
    # What we do:
    joltage_list.sort()
    joltage_list.insert(0, 0)
    joltage_list.append(builtin_joltage_adapter)
    linkers = {n: 1 for n in joltage_list} # Create dict where key=1 and value is jolt
    for idx, jolt in enumerate(joltage_list): # Loop for every jolt in our list
        for j in (idx + 2, idx + 3):
            if j < len(joltage_list) and joltage_list[j] - jolt <= 3:
                for jolt_2 in joltage_list[j:]:
                    linkers[jolt_2] += linkers[jolt]

    print(linkers[max(joltage_list)])

    # TODO: learn memoization


if __name__ == "__main__":
    part_1()
    part_2()