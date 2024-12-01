#!/usr/bin/env python3

################
# first part
################

the_File = "./in_data/1"

with open(the_File, "r") as f:
    contents = f.readlines()

# smallest number in left list with smallest number in right list
# then second-smallest, etc.

def column_split(contents: list):
    left = []
    right = []
    for line in contents:
        x = line.split(" ")
        left.append(x[0])
        right.append(x[-1].strip())
    return sorted(left), sorted(right)

# then, within each pair, figure distances between them
# then figure total distance(s) between both lists

def differencer(left: list, right: list):
    out = []
    for x in zip(left, right):
        i, j = int(x[0]), int(x[-1])
        if i >= j:
            out.append(i -j)
        else:
            out.append(j -i)
    return out

#differences = differencer(left_list, right_list)
#print(sum(differences))
# 1530215

###############
# second part
###############

# how often does each number from the left list appear in the right list
# then multiply that number by the times it appears in right list for similarity score

left_list, right_list = column_split(contents)

def counter(left: list, right: list):

    output = []
    skipper = []
    for x in left:
        if x in skipper:
            pass
        elif x in right:
            skipper.append(x)
            y = 0
            for n in right:
                if n == x:
                    y += 1
            output.append({x:y})
    return output

c = counter(left_list, right_list)

o = []
for x in c:
    for k, v in x.items():
        o.append(int(k) * int(v))
print(sum(o))

#26800609
