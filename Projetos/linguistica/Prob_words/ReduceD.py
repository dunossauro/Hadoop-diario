#!/usr/bin/env python3
from sys import stdin

##Print de apresentação e indicação
print (("Nº |%-20s%s|%-7s|%s") % ("Frase", " " * 8, "Prob", "Cont"))
print (("%s+%s+%s+%s") % ("-"*3, "-" * 28,"-" * 7 ,"-" * 5))

#Variáveis de contagem e organização
palavra_corrente = None
contador_corrente = 0
palavra = None
contador_total = 0
dicionario = {}

#Iteração para contagem
for linha in stdin:
    contador_total += 1
    linha = linha.strip()
    palavra_1, palavra_2, contador = linha.split() #Split das palavras vinda do shuffle para contagem

    palavra = (("%s %s") % (palavra_1, palavra_2)) #Junção das palavras, separadas de seu contador
    contador = int(contador)

    #validação para saber se ainda estamos na mesma palavra
    if palavra_corrente == palavra:
        contador_corrente += int(contador)

    #Caso não seja é atribuída a um dicionário a palavra e seu contador
    else:
        if palavra_corrente:
            dicionario[palavra_corrente] = contador_corrente
        contador_corrente = contador
        palavra_corrente = palavra

if palavra_corrente == palavra: #Print da ultima iteração
    dicionario[palavra_corrente] = contador_corrente

#print (('%-20s|%2s') %("Total",contador_total))

#Iteração sobre o dicionário para exibição em ordem alfabética, pode ser substituído por ordem de porcentagem
for y,x in enumerate(sorted(dicionario)):
    print(('%s  |\t%-20s\t|%5s%%\t|%5s')%(y,x, int(dicionario[x]/contador_total*100),dicionario[x]))
