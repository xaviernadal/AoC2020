with open("day1/input.txt") as f:
    number = f.readlines()
    number = list(map(int, number))

def part1():
    for i in number:
        for j in number:
            if i + j == 2020:
                return i * j

def part2():
    for i in number:
        for j in number:
            for k in number:
                if i + j + k == 2020:
                    return i * j * k

if __name__ == "__main__":
    print(part1())
    print(part2())
