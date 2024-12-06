#!/usr/bin/env python3

## reports, one per line
# separated by spaces
# each report is a list of numbers called levels

# find the count of safe reports
# a safe report is a list where each adjacent number:
# differs by at least one and at most three

data_input = "./in_data/2"
with open(data_input, "r") as f:
    contents = f.read().splitlines()

def decreasing(line):
    counter = 1
    for i, x in enumerate(line):
        if i >= 1:
            newx, newy = int(x), int(line[i - 1])
            if (newy - newx) <= 3 and (newy - newx) > 0:
                counter += 1
    return True if counter == len(line) else False

def increasing(line):
    counter = 1
    for i, x in enumerate(line):
        if i >= 1:
            newx, newy = int(x), int(line[i - 1])
            if (newx - newy) <= 3 and (newx - newy) > 0:
                counter += 1
    return True if counter == len(line) else False

def main(content):
    counter = 0
    for line in content:
        xline = line.split(" ")
        tst, case = xline[0], xline[1]
        if tst == case:
            pass
        elif int(tst) > int(case):
            if decreasing(xline):
                counter += 1
                print(line)
        elif int(case) > int(tst):
            if increasing(xline):
                counter += 1
        else:
            print("uh oh")
    return counter

#print(main(content=contents))
# 356
#################
## second part
#################
