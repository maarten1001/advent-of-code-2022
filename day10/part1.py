def process_input():
    with open("input.txt") as f:
        entries = f.read().splitlines()
        return entries


if __name__ == "__main__":
    total = 0
    X = 1
    cycle = 0
    target_cycles = range(20, 220 + 1, 40)
    counter = 0
    stack = None
    program = process_input()
    while True:
        cycle += 1
        if counter >= len(program):
            break
        # print(f"Start of cycle {cycle}")
        if stack is None:
            op = program[counter]
            # print(op)
            if op == "noop":
                stack = [1, op]
            else:
                stack = [2, op]
        # print(f"During cycle {cycle}, X is {X}")
        if cycle in target_cycles:
            signal_strength = cycle * X
            print(f"{cycle} * {X} = {signal_strength}")
            total += signal_strength
        stack[0] -= 1
        if stack[0] == 0:
            op = stack[1]
            stack = None
            counter += 1
            if op == "noop":
                pass
            else:
                op, value = op.split()
                X += int(value)
        # print(f"End of cycle {cycle}")
        # print(f"After cycle {cycle}, X is {X}")
    print(f"total = {total}")
