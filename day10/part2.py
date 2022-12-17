def process_input():
    with open("input.txt") as f:
        entries = f.read().splitlines()
        return entries


if __name__ == "__main__":
    screen = ""
    X = 1
    cycle = 0
    counter = 0
    stack = None
    program = process_input()
    while True:
        cycle += 1
        if counter >= len(program):
            break
        if stack is None:
            op = program[counter]
            if op == "noop":
                stack = [1, op]
            else:
                stack = [2, op]
        pixel = (cycle - 1) % 40
        if pixel == X - 1 or pixel == X or pixel == X + 1:
            screen += "#"
        else:
            screen += "."
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

    for i in range(0, len(screen), 40):
        print(screen[i:i + 40])
