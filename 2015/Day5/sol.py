import re

# Regex is a pain in the ass


def check_forbidden(input: str) -> bool:
    for naughty in ["ab", "cd", "pq", "xy"]:
        if naughty in input:
            return False

    return True


def check_vowels(input: str) -> bool:
    a = input.count("a")
    e = input.count("e")
    i = input.count("i")
    o = input.count("o")
    u = input.count("u")

    return a + e + i + o + u >= 3


def check_doubles(input: str) -> bool:
    for i, c in enumerate(input):
        try:
            if input[i + 1] == c:
                return True
        except IndexError:
            pass
    return False


def check_nice(input: str) -> bool:
    return check_forbidden(input) and check_vowels(input) and check_doubles(input)


def check_pairs(input: str) -> bool:
    # I cannot describe how long it took me to spot the misplaced closing
    # parenthesis on this !@#$ing capture group
    pairs = re.compile(r"([a-z]{2})[a-z]*\1")
    match = pairs.findall(input)
    return len(match) > 0


def check_repeat(input: str) -> bool:
    repeats = re.compile(r"([a-z])[a-z]\1")
    match = repeats.findall(input)
    return len(match) > 0


def check_nice_two(input: str) -> bool:
    return check_pairs(input) and check_repeat(input)


def part_one(data: list[str]):
    count = 0
    for line in data:
        if check_nice(line):
            count += 1
    return count


def part_two(data: list[str]):
    count = 0
    for line in data:
        if check_nice_two(line):
            count += 1
    return count


with open("2015/Day5/input.txt", "r") as file:
    data = file.readlines()

print(part_one(data))
print(part_two(data))
