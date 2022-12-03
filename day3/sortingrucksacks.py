file = open("/Users/adamgibbons/dev/adventofcode2022/day3/input.txt")
lines = file.readlines()

count = 0
lcl = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ucl = []
for l in lcl:
    ucl.append(l.upper())


def getScore(letter):
    if letter in lcl:
        return lcl.index(letter) + 1
    elif letter in ucl:
        return ucl.index(letter) + 27


for line in lines:

    pt1 = set(line[:len(line)//2])
    pt2 = set(line[len(line)//2:len(line)-1])

    for i in pt1:
        for j in pt2:
            if (i == j):
                count += getScore(i)

print(count)
