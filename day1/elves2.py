from functools import reduce

file = open("input.txt")
lines = file.readlines()

count = 0
highest = [3, 2, 1]

for line in lines:
    if line == "\n":
        count = 0
        continue

    count += int(line)
    
    highest.sort(reverse=True)
    for val in highest:
            
        if count > val:
            highest.remove(val)
            highest.append(count)

print(highest)
print(reduce(lambda a, b: a + b, highest))