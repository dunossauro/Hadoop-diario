#!/usr/bin/env python3

import sys

mes_val = {'01':0,'02':0,'03':0,'04':0,
           '05':0,'06':0,'07':0,'08':0,
           '09':0,'10':0,'11':0,'12':0,}

#Interação sobre a entrada padrão
for linha in sys.stdin:
    linha = linha.strip()
    data, var = linha.split()
    var = float(var) #O valor da variável de entrada é tratado como um float
    data_mes = data[4:6]

    #Iteração sobre o dicionário, para o caso dos meses não virem estruturados
    for x in mes_val:
        if x == data_mes:
            mes_val[x] += var

#Print no formato comum para o GNUPLOT
print(data[0:4]+"01\t", (mes_val['01']/31)/24)
print(data[0:4]+"02\t", (mes_val['02']/28)/24)
print(data[0:4]+"03\t", (mes_val['03']/31)/24)
print(data[0:4]+"04\t", (mes_val['04']/30)/24)
print(data[0:4]+"05\t", (mes_val['05']/31)/24)
print(data[0:4]+"06\t", (mes_val['06']/30)/24)
print(data[0:4]+"07\t", (mes_val['07']/31)/24)
print(data[0:4]+"08\t", (mes_val['08']/31)/24)
print(data[0:4]+"09\t", (mes_val['09']/30)/24)
print(data[0:4]+"10\t", (mes_val['10']/31)/24)
print(data[0:4]+"11\t", (mes_val['11']/30)/24)
print(data[0:4]+"12\t", (mes_val['12']/31)/24)
