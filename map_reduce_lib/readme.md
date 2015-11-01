#map_reduce_lib

É uma tentativa de facilidar as entradas do HDFS e também do Hadoop Streaming usando Python

####Funções básicas do HDFS:
```
  import map_reduce_lib as mrl
  
  mrl.hdfs_ls(dir)                #Lista o seu hdfs
  mrl.hdfs_rm(file)               #Remove seu arquivo
  mrl.hdfs_rm_dir(dir)            #Remove um diretório
  mrl.hdfs_mkdir(dir)             #Cria um diretório
  mrl.hdfs_put(file, dir)         #Insere um arquivo no diretório
  mrl.hdfs_get(dir, nome)         #Tranfere um arquivo do HDFS para o diretório local
  mrl.hdfs_format()               #Formata o seu NameNode
```  

####Função MapReduce:
```
  import map_reduce_lib as mrl
  
  mrl.run_map_reduce(mapper,reducer,_input,_output) #Função para executar o streaming de uma forma simples.
```

####Funções Hadoop:
```
  import map_reduce_lib as mrl
  
  hadoop_run(status)          #O status pode ser definido como start ou stop
```
