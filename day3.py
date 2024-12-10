#!/usr/bin/env python3

import re

with open("./in_data/3", "r") as f:
    contents = f.read()

matcher = re.compile(r"mul\((\d{1,3},\d{1,3})\)")

def mulper(x ,y):
    return x * y

def extracter(cs: str, xr=matcher):
    return xr.findall(cs)

def exgetr(xtracted: list):
    output = 0
    for x in xtracted:
        xx = x.split(",")
        factor = mulper(int(xx[0]), int(xx[1]))
        output += factor
    return output

def lastpart(x):
    return x[-1]

extracted = extracter(contents) # all of the numbers, in str 'x,y' format
out = exgetr(extracted)
print(f"First total: {out}")
# 179834255

##############################
## part two
##############################

dodo = re.compile(r"(do\(\))")
dont = re.compile(r"(don\'t\(\))")
matcher2 = re.compile(r"(don't\(\)|do\(\))")
matcher4 = re.compile(r"(do\(\)|don\'t\(\))(.*?)\s?(mul\((\d{1,3},\d{1,3})\))")
remover = re.compile(r"\[|from\(\)|\$|\#|!|<|>|why|\-|\?\]|who|where|~|\;|select|when|what|\:|how\(\)|\@|\&|\^|\'|\+")

def resubcleaner(c: str=contents, xr=remover):
    return xr.sub("", c)

cleaned = resubcleaner()
ex_all = extracter(cleaned, xr=matcher)

def bitchdick(cleaned):

    muls = matcher.findall(cleaned)
    donts = dont.findall(cleaned)
    dos = dodo.findall(cleaned)
    return muls, donts, dos

muls, donts, dos = bitchdick(cleaned)
if len(muls) != len(ex_all):
    print("Warning- length issue")

mdn = re.compile(r"(mul\(\d{1,3}\,\d{1,3}\))|(do\(\))|(don\'t\(\))")
newone = extracter(contents, xr=mdn)

def clean_newone(newone):
    out = []
    for x in newone:
        for y in x:
            if y:
                out.append(y)
    return out

newcleaned = clean_newone(newone)

def dingdong(nc: list):
    which_list = True
    doout = []
    dontout = []
    mdo = []

    for x in nc:
        if x.startswith("don't()"):
            which_list = False
            dontout.append(x)
        elif x.startswith("do("):
            which_list = True
            doout.append(x)
        else:
            if which_list:
                mdo.append(x)
            else:
                pass
    return mdo, doout, dontout

mdo, doout, dontout = dingdong(newcleaned)

def finalding(l):
    out = 0
    for x in l:
        rx = x.replace("mul(", "")
        ry = rx[:-1].split(",")
        newx, newy = int(ry[0]), int(ry[1])
        out += mulper(newx, newy)
    return out

print(finalding(mdo))
# 80570939
