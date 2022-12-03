with open("input.txt") as f:
    entries = f.read().splitlines()

total = 0
for i in range(0, len(entries), 3):
    if len(entries) % 3 != 0:
        print(f"Not all groups have three Elves")
        exit(1)
    for c in entries[i]:
        if c in entries[i + 1] and c in entries[i + 2]:
            if c.islower():
                priority = ord(c) - ord('a') + 1
            else:
                priority = ord(c) - ord('A') + 27
            print(f"{priority} ({c})")
            total += priority
            break
print(total)
