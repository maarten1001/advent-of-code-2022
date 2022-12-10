def process_input():
    with open("input.txt") as f:
        entries = f.read().splitlines()
        return entries[0]


if __name__ == "__main__":
    buffer = process_input()
    marker_length = 14
    for i in range(len(buffer) - marker_length + 1):
        char = buffer[i:i + marker_length]
        print(char)
        charset = set()
        for c in char:
            charset.add(c)
        if len(charset) == marker_length:
            print(i + marker_length)
            break
