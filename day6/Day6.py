answer_yes = []
count = 0
with open("day6/input.txt") as f:
    for line in f:
        if line != "\n":
            line = line.strip()
            for elem in line:
                if elem not in answer_yes:
                    answer_yes.append(elem)
                    count +=1
        else:
            answer_yes = []
print(count)

answer_yes = []
person_counter = 0
counter = 0
with open("day6/test.txt") as f:
    for line in f:
        if line != "\n":
            person_counter +=1
            line = line.strip()
            for elem in line:
                answer_yes.append(elem)
        else:
            results = dict((x,answer_yes.count(x)) for x in set(answer_yes))
            for value in results.values():
                if value == person_counter:
                    counter +=1
            print(results)
            person_counter = 0
            answer_yes = []

print(counter)
