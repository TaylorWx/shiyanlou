#!/usr/bin/env python
#-*- coding: gbk -*-
from difflib import Differ
from binascii import unhexlify

data1, data2 = [], []
sep = "   "

f = open("deltas\\delta.txt", "r")
for line in f:
    sep_pos = line.rfind(sep)
    data1.append(line[:sep_pos] + "\n")
    data2.append(line[sep_pos + len(sep):])    
f.close()

d = Differ()
result = list(d.compare(data1, data2))

f = open("delta.png", "wb")
f1 = open("delta1.png", "wb")
f2 = open("delta2.png", "wb")
for line in result:
    if line[0] == "+":
        f1.write(unhexlify(line.strip("\n+").replace(" ", "")))
    elif line[0] == "-":
        f2.write(unhexlify(line.strip("\n-").replace(" ", "")))
    else:
        f.write(unhexlify(line.strip().replace(" ", "")))
f.close()
f1.close()
f2.close()

