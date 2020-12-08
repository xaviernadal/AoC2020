with open("day8/input.txt") as f:
    instructions = f.readlines()
    
def part1():
    acc = 0
    index_list = []
    index = 0
    while index not in index_list:
        index_list.append(index)
        instr = instructions[index].strip().split()
        action = instr[0]
        number = instr[1]
        if action == "acc":
            acc += int(number)
            index +=1
        if action == "jmp":
            index += int(number)
        if action == "nop":
            index +=1
        
    print(acc)

def part2():
    acc_list = []
    for i in range(len(instructions)):
        acc = 0
        index_list = []
        new_instructions = []
        new_instructions = instructions.copy()
        index = 0
        instr = new_instructions[i].strip().split()
        action = instr[0]
        number = instr[1]
        if action == "jmp":
            action = "nop"
        elif action == "nop":
            action = "jmp"
        else:
            continue
        new_instructions[i] = action + " " + number
        while index not in index_list:
            if index == len(new_instructions):
                acc_list.append(acc)
                break
            index_list.append(index)
            instr = new_instructions[index].strip().split()
            action = instr[0]
            number = instr[1]
            if action == "acc":
                acc += int(number)
                index +=1
            if action == "jmp":
                index += int(number)
            if action == "nop":
                index +=1    

    print(acc_list)
if __name__ == "__main__":
    part1()
    part2()