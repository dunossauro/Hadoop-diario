#!/usr/bin/env python3

import sys

for linha in sys.stdin:
   linha = linha.strip()
   dados = linha.split()

    if int(dados[1]) < 10:
       dados[1] = str("0" + dados[1])

    if dados[0][6:10] == "2012":
        data = (("%s%s%s") % (dados[0][6:10],dados[0][3:5],dados[0][0:2]))

        hora,tmed,tmin,tmax,vento,chuva = \
        dados[1],dados[2].replace(",","."),dados[3].replace(",","."),dados[4].replace(",","."),dados[14].replace(",","."),dados[18].replace(",",".")

        print(("%s\t\t%s")%(data, tmed))
