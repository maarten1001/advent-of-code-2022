with open("input.txt") as f:
    entries = f.read().splitlines()

total = 0
for e in entries:
    if len(e) % 2 != 0:
        print(f"Unable to split odd number of items in {e}")
        exit(1)
    first_half = e[:len(e)//2]
    second_half = e[len(e)//2:]
    for c in first_half:
        if c in second_half:
            if c.islower():
                priority = ord(c) - ord('a') + 1
            else:
                priority = ord(c) - ord('A') + 27
            print(f"{priority} ({c})")
            total += priority
            break
print(total)
