#!/usr/bin/env python3

from sys import stdin, argv
from re import compile

regex = compile("\w+")
palavra = argv[1].lower()

for linha in stdin:
    linha = regex.findall(linha)

    linha = [e.lower() for e in linha]

    if palavra in linha:
        index = linha.index(palavra)
        try:
            print("{palavra} {palavra_seg}\t1".format(palavra=linha[index], palavra_seg=linha[index+1]))
        except:
            print("{palavra} {palavra_seg}\t1".format(palavra=linha[index], palavra_seg="."))
