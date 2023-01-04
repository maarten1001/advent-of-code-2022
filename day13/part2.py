def process_input():
    with open("input.txt") as f:
        entries = f.read().splitlines()
        entries = [x for x in entries if x != '']
        return entries


def check_order(left, right):
    for i in range(max(len(left), len(right))):
        left_value = left[i]
        right_value = right[i]

        integer_length = 1
        if left_value.isdecimal():
            while left[i + integer_length].isdecimal():
                left_value = left_value + left[i + integer_length]
                integer_length += 1
        if right_value.isdecimal():
            integer_length = 1
            while right[i + integer_length].isdecimal():
                right_value = right_value + right[i + integer_length]
                integer_length += 1

        if left_value == right_value:
            if left_value.isdecimal():
                return check_order(left[i + integer_length:], right[i + integer_length:])
            continue

        if left_value.isdecimal() and right_value.isdecimal():
            if int(left_value) < int(right_value):
                return True
            else:
                return False

        if left_value.isdecimal() and right_value == '[':
            if left[i + 1].isdecimal():
                return check_order('[' + left_value + ']' + left[i + 2:], right[i:])
            else:
                return check_order('[' + left_value + ']' + left[i + 1:], right[i:])

        if left_value == '[' and right_value.isdecimal():
            if right[i + 1].isdecimal():
                return check_order(left[i:], '[' + right_value + ']' + right[i + 2:])
            else:
                return check_order(left[i:], '[' + right_value + ']' + right[i + 1:])

        if left[i] == ']':
            return True

        if right[i] == ']':
            return False

        raise Exception(f"Unable to compare {left_value} and {right_value}")


def insertion_sort(array):
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0 and not check_order(array[j], key_item):
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item
    return array


def solve():
    packet1 = '[[2]]'
    packet2 = '[[6]]'
    packets = process_input()
    packets.extend([packet1, packet2])

    packets = insertion_sort(packets)
    index1 = packets.index(packet1) + 1
    index2 = packets.index(packet2) + 1
    print(index1 * index2)


if __name__ == "__main__":
    solve()
