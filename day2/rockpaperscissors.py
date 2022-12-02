file = open("input.txt")
lines = file.readlines()

score = 0

# PT.1

# AX = 4
# AY = 8
# AZ = 3
# BX = 1
# BY = 5
# BZ = 9
# CX = 7
# CY = 2
# CZ = 6

# PT.2

AX = 3
AY = 4
AZ = 8
BX = 1
BY = 5
BZ = 9
CX = 2
CY = 6
CZ = 7


def getScore(game):
    global score
    if game == "A X":
        score += AX
    elif game == "A Y":
        score += AY
    elif game == "A Z":
        score += AZ
    elif game == "B X":
        score += BX
    elif game == "B Y":
        score += BY
    elif game == "B Z":
        score += BZ
    elif game == "C X":
        score += CX
    elif game == "C Y":
        score += CY
    elif game == "C Z":
        score += CZ


for line in lines:
    getScore(line.rstrip())

print(score)
