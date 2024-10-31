from helpers import readfile


def solve(filename: str) -> int:
    suma = 0
    l = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    line_list = readfile(filename)
    for line in line_list:
        num = ""
        for i, c in enumerate(line):
            if c.isdigit():
                num = num + c
            else:
                for k in l.keys():
                    lookup = line[i : i + len(k)]
                    if lookup == k:
                        num = num + l[k]
                        break
        if len(num) == 1:
            suma = suma + int(num[0] + num[0])
        else:
            suma = suma + int(num[0] + num[-1])

    print(suma)
    return suma


# Tests
assert solve("data/day1test") == 142, "Coordinates should be 142"
assert solve("data/day1test2") == 281, "Coordinates should be 281"


solve("data/day1")
