import map_reduce_lib as mrl 

mrl.hdfs_rm_dir("data")
mrl.hdfs_mkdir("data")
mrl.hdfs_put("algumapoesia/*", "data")
mrl.hdfs_rm_dir("saida")

#Rodando o streaming
mrl.run_map_reduce("map.py","reduce.py","/data","/saida")
