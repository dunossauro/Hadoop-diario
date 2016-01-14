#!/bin/bash
##	inmet-Streaming 0.5

#Removendo a reduncancia, caso a pasta exista
/usr/local/hadoop/bin/hadoop fs -rm -r /saida

#Crianda a pasta de entrada e tranferindo os arquivos
/usr/local/hadoop/bin/hadoop fs -put dados_diarios.txt /data

/usr/local/hadoop/bin/hadoop jar \
/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
-mapper `pwd`/map.py \
-reducer `pwd`/reduce.py \
-input /data/* \
-output /saida

#Copia os arquivos de saída, caso exista mais de um
/usr/local/hadoop/bin/hadoop fs -get /saida/p*

#Move o arquivo para um nome conhecido
mv part-00000 saida.txt
