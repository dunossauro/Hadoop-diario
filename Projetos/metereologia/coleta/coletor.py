from os import system

ano = []
num_ano = range(17, 100)
for x in num_ano:
	ano.append(x)

num_ano = range(2000, 2015)
for x in num_ano:
	ano.append(x)


for x in ano:
	if x < 2000:
		dado = 'wget http://www.leb.esalq.usp.br/exceldados/ROB%s.xls' %(x)

	else:
		dado = 'wget http://www.leb.esalq.usp.br/exceldados/DCE%s.xls' %(x)
	
	system(dado)
