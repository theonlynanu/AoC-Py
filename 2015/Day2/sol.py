import math
import re

pattern = re.compile(r"(\d+)x(\d+)x(\d+)")


class Box:
    def __init__(self, width: int, height: int, length: int):
        self.width = width
        self.height = height
        self.length = length

    @property
    def surface(self) -> int:
        surface_area = (
            2 * self.length * self.width
            + 2 * self.length * self.height
            + 2 * self.width * self.height
        )

        slack = min(
            [
                self.length * self.width,
                self.length * self.height,
                self.height * self.width,
            ]
        )

        return surface_area + slack


def parse_line(line: str) -> Box:
    match = pattern.match(line)

    if not match:
        raise ValueError(f"Could not parse line: {line}")

    groups = match.groups()

    return Box(int(groups[0]), int(groups[1]), int(groups[2]))


def get_ribbon_length(box: Box) -> int:
    dimensions = sorted([box.width, box.height, box.length])

    ribbon = (2 * dimensions[0]) + (2 * dimensions[1])
    bow = math.prod(dimensions)

    return ribbon + bow


def part_one(lines: list[str]) -> int:
    sum = 0
    for line in lines:
        box = parse_line(line)
        sum += box.surface

    return sum


def part_two(lines: list[str]) -> int:
    sum = 0
    for line in lines:
        box = parse_line(line)
        sum += get_ribbon_length(box)

    return sum


with open("2015/Day2/input.txt", "r") as file:
    data = file.readlines()

print(part_one(data))
print(part_two(data))
