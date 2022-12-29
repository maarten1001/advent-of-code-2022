def process_input():
    with open("input.txt") as f:
        entries = f.read().splitlines()
        return entries


def compare(left, right):
    print(f"Compare {left}\nvs      {right}")
    for i in range(max(len(left), len(right))):
        left_value = left[i]
        right_value = right[i]
        # print(f"Compare {left_value} vs {right_value}")

        if left_value.isdecimal() and left[i + 1].isdecimal():
            left_value = str(10 * int(left_value) + int(left[i + 1]))
        if right_value.isdecimal() and right[i + 1].isdecimal():
            right_value = str(10 * int(right_value) + int(right[i + 1]))

        if left_value == right_value:
            if left_value.isdecimal():
                print(f"Compare {left_value} vs {right_value}")
            continue

        if left_value.isdecimal() and right_value.isdecimal():
            if int(left_value) < int(right_value):
                print("Left side is smaller, so inputs are in the right order")
                return True
            else:
                print("Right side is smaller, so inputs are not in the right order")
                return False

        if left_value.isdecimal() and right_value == '[':
            print(f"Mixed types; convert left to [{left_value}] and retry comparison")
            if left[i + 1].isdecimal():
                return compare('[' + left_value + ']' + left[i + 2:], right[i:])
            else:
                return compare('[' + left_value + ']' + left[i + 1:], right[i:])

        if left_value == '[' and right_value.isdecimal():
            print(f"Mixed types; convert right to [{right_value}] and retry comparison")
            if right[i + 1].isdecimal():
                return compare(left[i:], '[' + right_value + ']' + right[i + 2:])
            else:
                return compare(left[i:], '[' + right_value + ']' + right[i + 1:])

        if left[i] == ']':
            print("Left side ran out of items, so inputs are in the right order")
            return True

        if right[i] == ']':
            print("Right side ran out of items, so inputs are not in the right order")
            return False

        raise Exception(f"Unable to compare {left_value} and {right_value}")


def solve():
    total = 0
    packets = process_input()
    for i in range(0, len(packets), 3):
        print(f"== Pair {i // 3 + 1} ==")
        if compare(packets[i], packets[i + 1]):
            total += i // 3 + 1
        print()
    print(total)


if __name__ == "__main__":
    solve()
