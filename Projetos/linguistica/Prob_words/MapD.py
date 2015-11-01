#!/usr/bin/env python3

import sys

for linha in sys.stdin:
    linha = linha.strip()
    palavras = linha.split()

    for x,y in enumerate(palavras):
        if y.lower() == "as":
            palavras[x+1] = palavras[x+1].lower().replace("!"," !")
            palavras[x+1] = palavras[x+1].replace("?"," ? ").replace(","," , ")
            palavras[x+1] = palavras[x+1].replace(";"," ; ").replace("..."," ... ")
            palavras[x+1] = palavras[x+1].replace(":"," : ").replace("("," ( ")
            palavras[x+1] = palavras[x+1].replace(")"," ) ").replace("."," . ").replace("\""," \" ")
            print (("%s\t%s\t1")%(palavras[x].lower(),palavras[x+1].split()[0]))
        else:
            pass
