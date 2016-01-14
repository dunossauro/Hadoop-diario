## Tratamento de massas de dados com Hadoop

Foram usados os dados disponíveis pela [ESAQ-USP](http://www.leb.esalq.usp.br/base.html) 
tanto da base automática quando convencional para cruzamento com as bases do INMET.

#### Objetivos
	1. Traçar medidas visuais (gráficos) expondo o cruzamento das medidas
	2. Trasformar a coleta armazenavel em um banco de dados
	3. Testar o desempenho do cluster criado para esse projeto

#### Softwares
	Hadoop 			2.6.0
	Slackware		14.1-64bits
	Python			3+
	MatPlotlib
	Sqlite			3
	MapReduceLib		0.1.0
	
#### Resultados

> Chuvas de 2012 #Tabela


Ano|Mês|Media Chuva
|---|---|---|
2012|01|22.056989247311847
2012|02|25.71874999999999
2012|03|23.48870967741937
2012|04|22.363888888888866
2012|05|18.596774193548395
2012|06|18.104999999999986
2012|07|17.554838709677412
2012|08|19.406317204301065
2012|09|21.693194444444448
2012|10|24.27620967741937
2012|11|23.11777777777778
2012|12|25.317473118279555

> Temperaturas 2012 #Grafico

![Alt text](https://lh6.googleusercontent.com/-B4E7O-7K1o0/VYD265TItdI/AAAAAAAADyQ/6_ONeYWkX9A/w1044-h519-no/alegria.jgp.png)


grafico de exibição de médias de chuva (2011 - 2014)
![Alt text](https://lh3.googleusercontent.com/-iiXVqnUsNnQ/VaSH8AKQ9eI/AAAAAAAAD5Q/4i-RwZN3U0s/w1044-h503-no/chuva.png)

#### Arquivos
[Script de coleta e transferencia do csv2txt](https://github.com/z4r4tu5tr4/Hadoop-diario/tree/master/Projetos/metereologia/coleta)
	
[Txt para o Slqite3](https://github.com/z4r4tu5tr4/Hadoop-diario/blob/master/Projetos/metereologia/txt_2_sqlite.py)
	
[Scripts de MapReduce](https://github.com/z4r4tu5tr4/Hadoop-diario/tree/master/Projetos/metereologia/cruzamento)
	
[Teste com a MapReduceLib](https://github.com/z4r4tu5tr4/Hadoop-diario/blob/master/Projetos/metereologia/cruzamento/cruzamento_plot.py)

[Teste com Hadoop streaming](https://github.com/z4r4tu5tr4/Hadoop-diario/blob/master/Projetos/metereologia/hadoop_map_reduce.sh)
