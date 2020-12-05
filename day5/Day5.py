punctuation = {"F": 0, "B": 1, "L": 0, "R": 1}
max_punctuation = 0
all_ids = []
points = 0
with open("day5/input.txt") as f:
    for line in f:
        line = line.strip()
        row = line[:7]
        column = line[7::]
        length_row = len(row)
        length_column = len(column)
        for i in range(length_row):
            points += 2 ** (length_row - i - 1) * punctuation[row[i]]
        points = points * 8
        for i in range(length_column):
            points += 2 ** (length_column - i - 1) * punctuation[column[i]]
        if points > max_punctuation:
            max_punctuation = points
        all_ids.append(points)
        points = 0


def part2():
    for i in range(max_punctuation):
        if i not in all_ids:
            pass_id = i
    return pass_id

print("Part 1:", max_punctuation)
print("Part 2:", part2())
