from typing import List
from helpers import readfile
import re
from math import prod


class Game:
    def __init__(self, id, red, blue, green) -> None:
        self.id = id
        self.red = red
        self.blue = blue
        self.green = green

    def max_red(self) -> int:
        return max(self.red)

    def max_green(self) -> int:
        return max(self.green)

    def max_blue(self) -> int:
        return max(self.blue)


def task_one(games: List[Game]) -> int:
    # Rules: n of cubes must be < than treshold
    red = 12
    green = 13
    blue = 14
    sum = 0

    for game in games:
        tr = game.max_red()
        tg = game.max_green()
        tb = game.max_blue()
        if tr <= red and tg <= green and tb <= blue:
            sum = sum + game.id

    print(f"Task one: {sum}")

    return sum


def task_two(games: List[Game]) -> int:
    sum = 0

    for game in games:
        tr = game.max_red()
        tg = game.max_green()
        tb = game.max_blue()

        sum = sum + prod([tr, tg, tb])

    print(f"Task two: {sum}")

    return sum


def solve(filename: str) -> List[int]:
    lines = readfile(filename)

    games = []

    for line in lines:
        split = line.split(":")
        game_id_search_res = re.search(r"\d+", split[0])
        game_id = int(game_id_search_res[0]) if game_id_search_res is not None else 0
        lam = lambda x: int(x.split(" ")[0])
        red_search = list(map(lam, re.findall(r"\d+ red", split[1])))
        green_search = list(map(lam, re.findall(r"\d+ green", split[1])))
        blue_search = list(map(lam, re.findall(r"\d+ blue", split[1])))
        games.append(Game(game_id, red_search, blue_search, green_search))

    one = task_one(games)

    two = task_two(games)

    return [one, two]


# Tests

# Task one
assert solve("data/day2test")[0] == 8, "Sum should be 8"

# Task two
assert solve("data/day2test")[1] == 2286, "Sum should be 2286"

solve("data/day2")
