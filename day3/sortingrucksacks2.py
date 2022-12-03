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


for i in range(0, len(lines)-1, 3):

    common_item = (set(lines[i].strip()) & set(lines[i+1].strip())
                   & set(lines[i+2].strip()))
    count += getScore(next(iter(common_item)))

print(count)
