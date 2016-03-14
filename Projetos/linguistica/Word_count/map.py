#!/usr/bin/env python3

from sys import stdin
from re import compile
from collections import Counter
regex = compile("\w+")

for i in stdin:
    dicio = Counter(regex.findall(i))
    for x in dicio:
        print(("%s\t%s")%(x,dicio[x]))
