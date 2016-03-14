#!/usr/bin/env python3
from multiprocessing.pool import ThreadPool as Pool
from multiprocessing.pool import ThreadPool as Pool
from sys import stdin
from re import compile
regex = compile("\w+")

print (("%-20s|%-7s\n%-20s+-%-7s") % ("Palavra", "Frequência","-" * 20, "-" * 7))
dic = {}

def worker(line):
    line = line.strip()
    word, count = line.split('\t')

    count = int(count)

    if word not in dic: dic[word] =  count

    else: dic[word] += count

pool = Pool(8)

for item in stdin:
    pool.apply_async(worker(item), item)

pool.close()
pool.join()

for x in sorted(dic):
    print (('%-20s|%2s') % (x, dic[x]))
