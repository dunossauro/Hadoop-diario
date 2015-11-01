#!/usr/bin/env python3

import sys

for linha in sys.stdin:
    linha = linha.strip()
    dados = linha.split()
    if int(dados[2]) < 10:
    	dados[2] = str("0" + dados[2])

    ano,mes,dia,tmed,urmed,vento,tmax,urmax,ventomax,tmin,urmin,chuva = \
    dados[0],dados[1],dados[2],dados[3].replace(",","."),dados[4].replace(",","."),dados[5].replace(",","."),dados[6].replace(",","."),dados[7].replace(",","."),dados[8].replace(",","."),dados[9].replace(",","."),dados[10].replace(",","."),dados[11].replace(",",".")

    if ano == "2012":
    	print (("%s%s%s\t\t%s") % (ano,mes,dia,vento))
