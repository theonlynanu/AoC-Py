# Very brute force - could be done more efficiently with a dictionary that keeps
# track of tuples and counts, which could be useful if we want to get houses that
# get a certain number of presents, not just a non-zero amount - I got lucky that
# this wasn't the case


def number_of_houses(directions: str):
    valids = [">", "<", "v", "^"]
    x, y = 0, 0
    houses = [(0, 0)]
    for dir in directions:
        if dir not in valids:
            raise ValueError(f"Invalid direction: {dir}")

        if dir == ">":
            x += 1
        elif dir == "<":
            x -= 1
        elif dir == "^":
            y += 1
        else:
            y -= 1

        if (x, y) not in houses:
            houses.append((x, y))
    return len(houses)


def number_of_houses_robo(directions: str):
    valids = [">", "<", "v", "^"]
    x1, y1 = 0, 0
    x2, y2 = 0, 0
    houses = [(0, 0)]
    for i, dir in enumerate(directions):
        if dir not in valids:
            raise ValueError(f"Invalid direction: {dir}")

        if i % 2 == 0:
            if dir == ">":
                x1 += 1
            elif dir == "<":
                x1 -= 1
            elif dir == "^":
                y1 += 1
            else:
                y1 -= 1

            if (x1, y1) not in houses:
                houses.append((x1, y1))
        else:
            if dir == ">":
                x2 += 1
            elif dir == "<":
                x2 -= 1
            elif dir == "^":
                y2 += 1
            else:
                y2 -= 1

            if (x2, y2) not in houses:
                houses.append((x2, y2))

    return len(houses)


with open("2015/Day3/input.txt", "r") as file:
    data = file.read()

print(number_of_houses(data))
print(number_of_houses_robo(data))
