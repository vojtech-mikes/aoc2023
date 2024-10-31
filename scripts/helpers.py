def readfile(filename: str) -> list[str]:
    with open(filename, "r") as file:
        return [line.rstrip() for line in file]
