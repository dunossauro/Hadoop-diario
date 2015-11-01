import map_reduce_lib as mrl
from plot import exibir

#mrl.hadoop_run("start")

def run(put,map,reduce,entrada,saida,nome):
	
	mrl.hdfs_rm_dir(entrada) 						#remover caso exista
	mrl.hdfs_mkdir(entrada)							#criar uma nova vazia
	mrl.hdfs_put(put, entrada)						#Insere os dados
	mrl.hdfs_rm_dir(saida)							#remover caso exista
	mrl.run_map_reduce(map,reduce,entrada,saida) 	#map_reduce
	mrl.hdfs_get("saida",nome)

run("dados_e.txt","map_e.py","reduce_e.py","data","saida","esalq_tmed_2012")
run("dados_i.txt","map_i.py","reduce_i.py","data","saida","inmet_tmed_2012")

exibir("esalq_tmed_2012.dat","inmet_tmed_2012.dat")
