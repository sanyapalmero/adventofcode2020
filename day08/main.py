from copy import deepcopy


def read_file():
    with open("input.txt") as f:
        return f.read().splitlines()


NOP = "nop"
ACC = "acc"
JMP = "jmp"


def part_1():
    acc = 0
    commands = read_file()
    
    index = 0
    history = []

    while True:
        if index in history:
            break

        history.append(index)
        
        command = commands[index]
        cmd, value = command.split()
        if cmd == NOP:
            index += 1
            continue
        elif cmd == JMP:
            jump_to = int(value)
            index += jump_to
            continue
        elif cmd == ACC:
            acc += int(value)
            index += 1

    print(acc)


def part_2():
    def _swap_nop_jmp(commands):
        for index, command in enumerate(commands):
            cmd, value = command.split()
            if cmd == NOP:
                commands_copied = deepcopy(commands)
                commands_copied[index] = " ".join([JMP, value])
                yield commands_copied
            elif cmd == JMP:
                commands_copied = deepcopy(commands)
                commands_copied[index] = " ".join([NOP, value])
                yield commands_copied


    commands = read_file()
    final_acc = 0
    for updated_commands in _swap_nop_jmp(commands):
        acc = 0
        index = 0
        history = []
        while True:
            if index < 0 or index > len(updated_commands) - 1:
                final_acc = acc
                break
            if index in history:
                break

            history.append(index)        
            command = updated_commands[index]
            cmd, value = command.split()
            if cmd == NOP:
                index += 1
                continue
            elif cmd == JMP:
                jump_to = int(value)
                index += jump_to
                continue
            elif cmd == ACC:
                acc += int(value)
                index += 1

    print(final_acc)



if __name__ == "__main__":
    part_1()
    part_2()