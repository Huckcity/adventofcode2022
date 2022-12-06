import re
file = open("C:\\dev\\adventofcode2022\\day6\\input.txt")
input = file.read()

for x in range(len(input)):
    current_group = list(input[x:x+14])
    if(len(set(current_group)) == len(current_group)):
        print(x+14)