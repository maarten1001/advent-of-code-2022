with open("input.txt") as f:
    entries = f.read().splitlines()
    empty_line = entries.index('')

    drawing = entries[:empty_line - 1]
    stack_numbers = entries[empty_line - 1]
    procedure = entries[empty_line + 1:]

stacks = [[]]
# check how many stacks we need
stack_count = len(stack_numbers.split())
for i in range(stack_count):
    stacks.append([])

chunk_size = 4
for i in range(len(drawing)-1, -1, -1):
    for j in range(len(drawing[i])):
        start = j * chunk_size
        chunk = drawing[i][start:start + chunk_size]
        chunk = chunk.strip()
        if chunk != '':
            stacks[j + 1].append(chunk)


def print_stack():
    highest_stack = max(len(x) for x in stacks)
    for j in range(highest_stack - 1, -1, -1):
        line = []
        for i in range(1, stack_count + 1):
            if j < len(stacks[i]):
                line.append(stacks[i][j])
            else:
                line.append('   ')
        print(' '.join(line))
    print(stack_numbers)
    print()


def move(count, src, dest):
    if count > len(stacks[src]):
        print(f"Cannot move {count} crates from stack {src}. "
              f"There are only {len(stacks[src])} crates in the stack")
        exit(1)
    index = len(stacks[src]) - count
    crates = stacks[src][index:]
    stacks[src] = stacks[src][:index]
    stacks[dest].extend(crates)


if __name__ == "__main__":
    print_stack()
    for p in procedure:
        p = p.split()
        move(int(p[1]), int(p[3]), int(p[5]))
        print_stack()

    message = ""
    for n in range(1, len(stacks)):
        message += stacks[n][-1][1]
    print(message)
