with open("AoC2020/day2/input.txt") as f:
    number = f.readlines()

def part1():
    counter = 0   
    count_letter = 0

    for i in number:
        parameters = i.split()
        repetition = (parameters[0].split("-"))
        letter = parameters[1].strip(":")
        password = parameters[2]
        count_letter = 0
        for j in password:
            if j == letter:
                count_letter +=1
        
        if count_letter >= int(repetition[0]) and count_letter <= int(repetition[1]):
            counter +=1
    print(counter)

def part2():
    counter = 0
    count_letters = 0
    for numero in number:
        parameters = numero.split()
        positions = (parameters[0].split("-"))
        letter = parameters[1].strip(":")
        password = parameters[2]
        count_letters = 0

        first_position = int(positions[0])-1
        second_position = int(positions[1])-1
        
        if password[first_position] == letter:
            count_letters +=1
        if password[second_position] == letter:
            count_letters +=1
            
        if count_letters == 1:
            counter +=1
    print(counter)

if __name__ == "__main__":
    part1()
    part2()

        
    
