import re

# Comments in this file are more for me than for you

squares = re.compile(r"(\d{1,3},\d{1,3}) through (\d{1,3},\d{1,3})")

with open("2015/Day6/input.txt", "r") as file:
    instructions = file.readlines()


# //The repetition here is annoying, but readable. I am tempted to change this,
# //using lambda functions and passing that callback to sequentially read and
# //execute each instruction on each cell
# def turn_on_set(cells: tuple(str)):
#     pass


# def turn_off_set(cells: tuple(str)):
#     pass


# def toggle_set(cells: tuple(str)):
#     pass


TURN_ON = lambda x: True
TURN_OFF = lambda x: False
TOGGLE = lambda x: not x


# TODO: use the typing library to sort this crap out
def parse_line(line: str):  # -> tuple(function(), tuple(int), tuple(int))
    # tuple(map(int, squares.findall("0,0 through 12,145")[0][n].split(",")))
    # Above returns the nth tuple of integers given an instruction set
    parsed = squares.findall(line)
    if not parsed:
        raise ValueError(f"Cell numbers not properly formatted: {line}")

    cells = parsed[0]
    start = tuple(map(int, cells[0].split(",")))
    end = tuple(map(int, cells[1].split(",")))

    if line.startswith("turn on"):
        return TURN_ON, start, end
    elif line.startswith("turn off"):
        return TURN_OFF, start, end
    elif line.startswith("toggle"):
        return TOGGLE, start, end
    else:
        raise ValueError(f"Could not read instruction: {line}")


def execute_instructions(instructions: list[str]) -> int:
    # Storing the lights in a dict rather than a two-dimensional array bc I don't hate myself

    lights: dict[tuple(int, int) : bool] = {}

    for line in instructions:
        action, start, end = parse_line(line)
        x_start, y_start = start
        x_end, y_end = end

        # As always, off-by-one mistakes in ranges are the death of me
        for x in range(x_start, x_end + 1):
            for y in range(y_start, y_end + 1):
                light = (x, y)

                if (x, y) not in lights:
                    lights[(x, y)] = False

                lights[light] = action(lights[light])

    return len({light: isOn for light, isOn in lights.items() if isOn})


def execute_part_two(instructions: list[str]):
    lights: dict[tuple(int, int) : int] = {}

    for line in instructions:
        action, start, end = parse_line(line)
        x_start, y_start = start
        x_end, y_end = end

        for x in range(x_start, x_end + 1):
            for y in range(y_start, y_end + 1):
                light = (x, y)

                if light not in lights:
                    lights[light] = 0

                # An alternative here is to use a unique parse_line_two() function
                # that returns an integer value instead of an callback function,
                # adds to current value, then floors to 0
                if action == TURN_ON:
                    lights[light] += 1
                elif action == TURN_OFF:
                    lights[light] = max(0, lights[light] - 1)
                elif action == TOGGLE:
                    lights[light] += 2
                else:
                    raise ValueError(f"Unknown instruction: {str(action)}")

    return sum(lights.values())


print(execute_instructions(instructions))
print(execute_part_two(instructions))
