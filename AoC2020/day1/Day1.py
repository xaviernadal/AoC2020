def part1():
    with open("day1/input.txt") as f:
        number = f.readlines()
        number = list(map(int, number))
        print(number)
    for i in number:
        for j in number:
            for k in number:
                if i + j + k== 2020:
                    return i * j * k


if __name__ == "__main__":
    print(part1())