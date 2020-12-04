with open("day3/input.txt") as f:
    lines = f.readlines()


def part1():
    line = lines[0].strip()
    length = len(line)
    punterX = 0
    counter = 0
    for line in lines:
        line = line.strip()
        if punterX >= length:
            punterX = punterX-length
        if line[punterX] == "#":
            counter +=1
        punterX +=3
    print(counter)

def part2():
    line = lines[0].strip()
    length = len(line)
    punterX = 0
    counter = 0
    results = 1
    instructions = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    loop = False
    for i in instructions:
        punterX = 0
        for line in lines:
            if i[1] == 2:
                if loop:
                    loop = False
                    continue
                if not loop:
                    loop = True
            line = line.strip()
            if punterX >= length:
                punterX = punterX-length
            if line[punterX] == "#":
                counter +=1
            punterX +=i[0]

            
            
        results = results * counter
        counter = 0
    
    print(results)

if __name__ == "__main__":
    part1()
    part2()