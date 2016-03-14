#!/usr/bin/env python3
from sys import stdin

print (("%-20s|%-7s\n%-20s+-%-7s") % ("Palavra", "Frequência","-" * 20, "-" * 7))
dic = {}

for line in stdin:
    line = line.strip()
    word, count = line.split('\t')

    count = int(count)

    if word not in dic:
        dic[word] =  count
    else:
        dic[word] += count

for x in sorted(dic):
    print (('%-20s|%2s') % (x, dic[x]))
