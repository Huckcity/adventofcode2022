file = open("input.txt")
lines = file.readlines()

count = 0

for line in lines:

    ranges = line.split(',')
    range1Lower = int(ranges[0].split('-')[0])
    range1Upper = int(ranges[0].split('-')[1])
    range2Lower = int(ranges[1].split('-')[0])
    range2Upper = int(ranges[1].split('-')[1].strip())

    # PT.1
    # if ((range1Lower <= range2Lower and range1Upper >= range2Upper)
    #         or (range2Lower <= range1Lower and range2Upper >= range1Upper)):
    #     count += 1

    # PT.2
    if ((range1Lower <= range2Lower and range1Upper >= range2Lower)
        or (range1Lower <= range2Upper and range1Upper >= range2Upper)
        or (range2Lower <= range1Lower and range2Upper >= range1Lower)
            or (range2Lower <= range1Upper and range2Upper >= range1Upper)):
        count += 1

print(count)
