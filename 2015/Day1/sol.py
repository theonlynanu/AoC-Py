def part_one(input_data: list[str]) -> int:
    floor = 0
    for char in input_data:
        if char == "(":
            floor += 1
        else:
            floor -= 1

    return floor


def part_two(input_data: list[str]) -> int:
    floor = 0
    pos = 1
    for char in input_data:
        if char == "(":
            floor += 1
        else:
            floor -= 1

        if floor == -1:
            return pos
        else:
            pos += 1
    return -1


if __name__ == "__main__":
    with open("2015\Day1\input.txt", "r") as file:
        data = file.read().replace("\n", "")

    print(part_one(data))
    print(part_two(data))
