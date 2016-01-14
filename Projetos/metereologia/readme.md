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

grafico de exibição de médias de chuva (2011 - 2014)
![Alt text](https://lh3.googleusercontent.com/-iiXVqnUsNnQ/VaSH8AKQ9eI/AAAAAAAAD5Q/4i-RwZN3U0s/w1044-h503-no/chuva.png)

#### Arquivos
[Script de coleta e transferencia do csv2txt](https://github.com/z4r4tu5tr4/Hadoop-diario/tree/master/Projetos/metereologia/coleta)
	
[Txt para o Slqite3]()
	
[Scripts de MapReduce](https://github.com/z4r4tu5tr4/Hadoop-diario/tree/master/Projetos/metereologia/cruzamento)
	
[Teste com a MapReduceLib](https://github.com/z4r4tu5tr4/Hadoop-diario/blob/master/Projetos/metereologia/cruzamento/cruzamento_plot.py)
