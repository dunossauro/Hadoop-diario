#!/usr/bin/python3

######################################
#	Script to usage python with HDFS #
#									 #
# Author: Eduardo Mendes			 #
# Git: Github.com/z4r4tu5tr4		 #
# Version: 0.1 						 #
# Date:	2015/AGO/17					 #
######################################

"""
	How it work?

	You can "import HDFS" and call your functions;
	or you can copy the script and past in your code

	Example:

	import HDFS

	HDFS.cat("<arq>.txt")
	HDFS.rm("<arq>")
	HDFS.rm_r("<dir>")
"""

from os import system

#Estrutura base
hadoop = "/usr/local/hadoop/bin/hadoop"
hdfs = "/usr/local/hadoop/bin/hadoop fs"
script = "/usr/local/hadoop/sbin/"

#Manipulação do HDFS
def cat(file):
	system(("%s -cat /%s")%(hdfs,file))

def chgrp(mode, file):
	system(("%s -chgrp %s /%s")%(hdfs,mode,file))

def chmod(mode,file):
	system(("%s -chmod %s /%s")%(hdfs,mode,file))

def chown(mode,file):
	system(("%s -chown %s /%s")%(hdfs,mode,file))

def copy_from_local(local, dst):
	system(("")%(hdfs,local,dst))

def copy_to_local():
	system(("")%(hdfs,))

def count():
	system(("")%(hdfs,))

def cp():
	system(("")%(hdfs,))

def du():
	system(("")%(hdfs,))

def dus():
	system(("")%(hdfs,))

def expunge():
	system(("")%(hdfs,))

def get(dir,nome):
		os.system(("%s -get /%s/part-00000 .")%(hdfs,dir))
		os.system(("mv part-00000 %s.dat")%(nome))

def get_merge():
	system(("")%(hdfs,))

def help():
	system(("")%(hdfs,))

def ls(dir):
		system(("%s -ls /%s")%(hdfs,dir))

def mkdir(dir):
		system(("%s -mkdir /%s")%(hdfs,dir))

def mv ():
	system(("")%(hdfs,))

def put(files,dir):
		system(("%s -put %s /%s")%(hdfs,files,dir))

def rm(dir):
		system(("%s -rm /%s")%(hdfs,dir))

def rm_dir(dir):
		system(("%s -rm -r /%s")%(hdfs,dir))

def setrep():
	system(("")%(hdfs,))

def stat():
	system(("")%(hdfs,))

def tail():
	system(("")%(hdfs,))

def test():
	system(("")%(hdfs,))

def touchhz():
	system(("")%(hdfs,))

def format():
	s_n = input("Deseja realmente formatar o seu HDFS? (S/N)")
	if s_n == "S" or "s":
		system("/usr/local/hadoop/bin/hdfs namenode -format")
