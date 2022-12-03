from functools import reduce

file = open("input.txt")
lines = file.readlines()

count = 0
vals = [0]

for line in lines:
    if line == "\n":
        vals.append(count)
        count = 0
    else:
        count += int(line)

vals.sort()
print(vals[-3:])
print(reduce(lambda a, b: a + b, vals[-3:]))
