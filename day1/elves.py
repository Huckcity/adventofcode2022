file = open("input.txt")
lines = file.readlines()

count = 0
highest = 0

for line in lines:
    if line == "\n":
        count = 0
        continue

    count += int(line)
    
    if count > highest:
        highest = count
        count = 0
        print(highest)
    continue

