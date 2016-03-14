#!/usr/bin/env python3
from multiprocessing.pool import ThreadPool as Pool
from sys import stdin
from collections import Counter
from re import compile
regex = compile("\w+")

def worker(line):
    line = line.strip()

    dicio = Counter(regex.findall(line))
    for x in dicio:
        print(("%s\t%s")%(x,dicio[x]))

pool_size = 4
pool = Pool(pool_size)

for item in stdin:
    pool.apply_async(worker(item), item)

pool.close()
pool.join()
