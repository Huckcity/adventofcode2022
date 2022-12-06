import re
file = open("input.txt")
lines = file.readlines()

stacks = [[],[],[],[],[],[],[],[],[]]
cleanStacks = []
for i in range(7,-1,-1):
    
    line = []
    
    for x in range(1, len(lines[i]), 4):
        line.append(lines[i][x])

    for j in range(len(stacks)):
        stacks[j].append(line[j])

for stack in stacks:
    newStack = [x for x in stack if x != ' ']
    cleanStacks.append(newStack)

for i in range(10, len(lines)):

    operationsStr = list(re.findall(r'\d+', lines[i]))
    operations = list(map(int, operationsStr))

    items_to_move = []
    items_to_move = cleanStacks[operations[1]-1][-operations[0]:]
    # reversed_items = items_to_move.reverse()

    for item in items_to_move:
        cleanStacks[operations[1]-1].pop()
        cleanStacks[operations[2]-1].append(item)

[print(stack) for stack in cleanStacks]
[print(stack[-1] if len(stack) > 0 else '') for stack in cleanStacks]

#RTGWZTHLD

#STHGRZZFR