"""
Entrada dos dados diários do esalq
Parte da proposta de um coletor, mas no memonto faz a inserção e busca dos dados do txt no banco

Usa python 3 + Sqlite 3
"""

import sqlite3
sql = 'SELECT * FROM dados_diarios WHERE ano = ?'

#conexão com o banco
con = sqlite3.connect('dados_diarios.db')
cur = con.cursor()

#criação da tabela
def c_table():
	cur.execute('CREATE TABLE IF NOT EXISTS dados_diarios \
		(ano integer, mes integer, dia integer, \
			tmed real, urmed real, vento real, tmax real, urmax real,\
			ventomax real, tmim real, urmim real, chuva real)')

def inter_d():
	import sys

	for linha in sys.stdin:
	    linha = linha.strip()
	    dados = linha.split()

	    ano,mes,dia,tmed,urmed,vento,tmax,urmax,ventomax,tmin,urmin,chuva = \
	    dados[0],dados[1],dados[2],dados[3].replace(",","."),dados[4].replace(",","."),dados[5].replace(",","."),dados[6].replace(",","."),dados[7].replace(",","."),dados[8].replace(",","."),dados[9].replace(",","."),dados[10].replace(",","."),dados[11].replace(",",".")

	    cur.execute('INSERT INTO dados_diarios (ano, mes, dia, tmed, urmed, vento, tmax,urmax, ventomax, tmim, urmim, chuva) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (ano,mes,dia,tmed,urmed,vento,tmax,urmax,ventomax,tmin,urmin,chuva))
	    con.commit()

def read_d():
	for x in cur.execute(sql, ('2000',)):
		print(x)

#c_table()
#inter_d()
read_d()
