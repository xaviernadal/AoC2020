bags = {}
with open("day7/input.txt") as f:
    data = [y.split(" contain ") for y in [x.strip() for x in f.read().splitlines()]]
    for bag in data:
        big_bag = [bag[0], bag[1].replace('bag.', 'bags.').replace('bag,','bags,').strip('.')] 
        bags[big_bag[0]] = {x[2:]:(int(x[0])) for x in bag[1].split(', ') if not x[0].isalpha()}

def part1():
    search_bags = ["shiny gold"]
    
    for _ in range(10):
        for item in bags:  
            bags_inside = bags[item]
            for bag in bags_inside:
                for any_bag in search_bags:
                    if any_bag in bag:
                        if item[:-1] not in search_bags:
                            search_bags.append(item[:-1])

    print(len(search_bags)-1)

def part2(bags_momentum):
    global count
    for k,v in bags_momentum.items():
        print(k, v)
        if k[-1] != "s":
            k = k + "s"
        if k[-2] == ".":
            k = k[:-2]
            if k[-1] != "s":
                k = k + "s"

        for _ in range(v):
            count += 1
            part2(bags[k])

    return count

if __name__ == "__main__":
    part1()
    count = 0
    print(part2(bags["shiny gold bags"] ))