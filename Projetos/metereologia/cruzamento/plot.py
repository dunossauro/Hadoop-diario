import matplotlib.pyplot as p

def exibir(arq1,arq2):
	meses = list(range(1,13))

	def arq(dat):
		arq = open(dat, 'r')

		var = []
		for x in arq:
			var.append(x[7:])

		arq.close()
		return(var)

	#medidas de 2012
	graf_1= arq(arq1)
	graf_2 = arq(arq2)


	#Fundo
	fig = p.figure()
	rect = fig.patch
	rect.set_facecolor('white')

	#Grafico 1.1
	ax1 = fig.add_subplot(2,1,1, axisbg='white')
	ax1.plot(meses,graf_1,'c', linewidth=4.0, linestyle='-')
	ax1.set_title(arq1)

	#Grafico 1.2
	ax2 = fig.add_subplot(2,1,2, axisbg='white')
	ax2.plot(meses,graf_2,'r', linewidth=4.0, linestyle='-')
	ax2.set_title(arq2)

	p.show()
