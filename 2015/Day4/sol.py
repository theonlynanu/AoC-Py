import hashlib


# def find_suffix(key: str, search_range: int) -> int:
#     for i in range(search_range):
#         hash = hashlib.md5((key + str(i)).encode("utf-8")).hexdigest()
#         if hash[:5] == "00000":
#             return i
#     raise ValueError("No number found in range")


def find_suffix(key: str, target: str, search_range: int) -> int:
    for i in range(search_range):
        hash = hashlib.md5((key + str(i)).encode("utf-8")).hexdigest()
        if hash[: len(target)] == target:
            return i

    raise ValueError(f"No match found in given range: {range}")


with open("2015/Day4/input.txt", "r") as file:
    key = file.read()


def part_one(data: str):
    return find_suffix(data, "00000", 1000000)


def part_two(data: str):
    return find_suffix(data, "000000", 10000000)


print(part_one(key), part_two(key))
