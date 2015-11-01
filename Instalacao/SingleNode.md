#Instalação e configuração do Hadoop Single node no Linux

##Instalação do Hadoop

####Modo convencional:
	
	Foi executado download da versão stable do hadoo (2.6.0 - Atual 13/abril/2014) 

####Disponível em:  
	http://mirror.nbtelecom.com.br/apache/hadoop/common/stable/

####Logo após nós podemos descompactar:
	
	tar xvvf hadoop*
	
####e mover para /usr/local/hadoop (o local recomendado por convenção):
	
	mv hadoop* /usr/local/hadoop
	
##Instalação em outras distribuições:

No caso, eu uso Arch linux. Então para instalar no Arch:
	
	yaourt -S hadoop
	
Existem maneira simples para executar a instalação no Debian, Ubuntu, Fedora (etc) apartir de alguns repositórios

##Instalação do java:
	
No caso ArchLinux:
	
	yaourt -S jdk8-openjdk

##Variáveis de ambiente

A configuração da variável do Java (ao meu ver) é um pouco chata, então pra evitar essa "maldição" podemos configurar o hadoop-env.sh:

	vim /usr/local/hadoop/etc/hadoop/hadoop-env.sh
	
e faremos a seguinte alteração na linha 25:
	
	export JAVA_HOME=<Caminho-de-instação-do-seu-Java>

no meu caso:
	export JAVA_HOME=/usr/lib/jvm/default

##Variável Hadoop

Para facilitar o manuseio dos arquivos do Hadoop, podemos criar algumas variáveis uteis ao Bash, como:


	HADOOP_INSTALL=/usr/local/hadoop
	HADOOP_BIN=/usr/local/hadoop/bin
	HADOOP_SBIN=//usr/local/hadoop/sbin
	
E para executarmos o hadoop de maneira simples, podemos criar uma direta ao executável do Hadoop:

	HADOOP=/usr/local/hadoop/bin/hadoop

##Pronto

Seu Hadoop está instalado com sucesso, suas variáveis estão configuradas de uma maneira inteligente. Agora temos que executar um teste básico, só pra verificar como as coisas estão

###Teste
 	
 	$ mkdir input
	$ cp $HADOOP_INSTALL/hadoop/etc/hadoop/*.xml input
	$ hadoop jar $HADOOP_INSTALL/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.6.0.jar grep input output 'dfs[a-z.]+'
	$ cat output/*

Se tudo aconteceu com sucesso, e apareceram algumas boas palavrias na tela, parabéns está tudo feito com sucesso.


##Referências:

```  
  1. https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/SingleCluster.html
  2. https://wiki.archlinux.org/index.php/Hadoop
  3. http://cute-jumper.github.io/linux/2014/09/05/install-hadoop-250-on-arch-linux/
  4. http://www.michael-noll.com/tutorials/running-hadoop-on-ubuntu-linux-single-node-cluster/
```
