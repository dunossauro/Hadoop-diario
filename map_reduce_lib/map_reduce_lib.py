import os

#Estrutura base
hadoop = "/usr/local/hadoop/bin/hadoop"
hdfs = "/usr/local/hadoop/bin/hadoop fs"
script = "/usr/local/hadoop/sbin/"

#Manipulação do HDFS
def hdfs_ls(dir):
	if dir:
		os.system(("%s -ls /%s")%(hdfs,dir))
	else:
		os.system(("%s -ls /")%(hdfs))
def hdfs_rm(dir):
	if dir:
		os.system(("%s -rm /%s")%(hdfs,dir))
def hdfs_rm_dir(dir):
	if dir:
		os.system(("%s -rm -r /%s")%(hdfs,dir))
def hdfs_mkdir(dir):
	if dir:
		os.system(("%s -mkdir /%s")%(hdfs,dir))
def hdfs_put(files,dir):
	if files and dir:
		os.system(("%s -put %s /%s")%(hdfs,files,dir))
def hdfs_get(dir,nome):
	if dir:
		os.system(("%s -get /%s/part-00000 .")%(hdfs,dir))
		os.system(("mv part-00000 %s.dat")%(nome))
def hdfs_format():
	s_n = input("Deseja realmente formatar o seu HDFS? (S/N)")
	if s_n == "S" or "s":
		os.system("/usr/local/hadoop/bin/hdfs namenode -format")

#Manipulação de funções de MapReduce
def run_map_reduce(mapper,reducer,_input,_output):
	
	os.system(("%s jar \
	/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.*.jar \
	-mapper `pwd`/%s \
	-reducer `pwd`/%s \
	-input /%s \
	-output /%s")%(hadoop,mapper,reducer,_input,_output))

#Start ou Stop Hadoop
def hadoop_run(status):
	if status == "stop":
		os.system(("%s/stop-all.sh")%(script))
	if status == "start":
		os.system(("%s/start-all.sh")%(script))
