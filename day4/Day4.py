total = []
passport = {}
with open("day4/input.txt") as f:
    for line in f:
        if line != "\n":
            line = line.strip().split()
            for elem in line:    
                passport[elem[:3]] = elem[4::]
        else:
            total.append(passport)
            passport = {}
count = 1
count2 = 1
for i in total:
    if "ecl" in i.keys() and "pid" in i.keys() and "eyr" in i.keys() and "hcl" in i.keys() and "byr" in i.keys() and "iyr" in i.keys() and "hgt" in i.keys():
        count +=1
        if int(i["byr"]) >= 1920 and int(i["byr"])<= 2002:
            if int(i["iyr"]) >= 2010 and int(i["iyr"]) <= 2020:
                if int(i["eyr"]) >= 2020 and int(i["eyr"]) <= 2030:
                    if i["hcl"][0] == "#" and len(i["hcl"]) == 7:
                        if i["ecl"] == "amb" or i["ecl"] == "blu" or i["ecl"] == "gry" or i["ecl"] == "grn" or i["ecl"] == "hzl" or i["ecl"] == "oth" or i["ecl"] == "brn":
                            if len(i["pid"]) == 9:
                                if i["hgt"][-2::] == "cm":
                                    if int(i["hgt"][:-2]) >= 150 and int(i["hgt"][:-2]) <= 193:
                                        count2 +=1
                                elif i["hgt"][-2::] == "in":
                                    if int(i["hgt"][:-2]) >= 59 and int(i["hgt"][:-2]) <= 76:
                                        count2 +=1
    
print("Part1: " + str(count))
print("Part2: " + str(count2))

                        