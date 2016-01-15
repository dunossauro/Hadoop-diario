#Configuração modo pseudo-distribuído no Linux

Para configurar o modo pseudo-distribuído você deve cofigurar o modo single anteriormente:
  
  [single](https://github.com/z4r4tu5tr4/Hadoop-diario/blob/master/Instalacao/SingleNode.md)

Por Default todas as jobs do hadoop são executadas pelo usuário 0 (root) e se você deseja que as operações sejam executadas em um user específico você pode setar em `/etc/conf.d/hadoop` alterando a linha:

>HADOOP_USERNAME = "<seu nome de usuário>"

E em seguida temos que configurar os xmls do hadoop e o ssh.

os arquivos xml estão localizados em `/usr/local/hadoop/etc/hadoop`

Logo após, juntei aqui arquivos básicos de configuração para subir e derrubar os serviços.

##Arquivos de configuração

###core-site.xml:

	<configuration>
		<property>
			<name>fs.defaultFS</name>
			<value>hdfs://localhost:9000</value>
		</property>
	</configuration>

###hdfs-site.xml:

	<configuration>
		<property>
	        	<name>dfs.replication</name>
	                <value>1</value>
		</property>
	        <property>
	        	<name>dfs.namenode.name.dir</name>
	                <value>file:/usr/local/hadoop/hadoop_data/hdfs/namenode</value>
		</property>
	        <property>
	        	<name>dfs.datanode.data.dir</name>
	                <value>file:/usr/local/hadoop/hadoop_store/hdfs/datanode</value>
		</property>
	</configuration>

###mapred-site.xml:

	<configuration>
		<property>
			<name>mapreduce.framework.name</name>
			<value>yarn</value>
		</property>
	</configuration>

###yarn-site.xml:


	<configuration>
		<property>
	        	<name>yarn.nodemanager.aux-services</name>
	                <value>mapreduce_shuffle</value>
		</property>
		<property>
	        	<name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name>
	                <value> org.apache.hadoop.mapred.ShuffleHandler</value>
		</property>
	</configuration>

##Conguração SSH

	ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
	cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
	ssh-keyscan -H localhost, localhost >> ~/.ssh/known_hosts
	ssh-keyscan -H localhost, 0.0.0.0 >> ~/.ssh/known_hosts

##Criação do script para subir os serviços:

	$HADOOP_INSTALL/hadoop-2.6.0/sbin/start-dfs.sh
	$HADOOP_INSTALL/hadoop-2.6.0/sbin/start-yarn.sh
	$HADOOP_INSTALL/hadoop-2.6.0/sbin/mr-jobhistory-daemon.sh start historyserver

##Criação do script para derrubar os serviços:

	$HADOOP_INSTALL/hadoop-2.6.0/sbin/mr-jobhistory-daemon.sh stop historyserver
	$HADOOP_INSTALL/hadoop-2.6.0/sbin/stop-yarn.sh
	$HADOOP_INSTALL/hadoop-2.6.0/sbin/stop-dfs.sh
	
##Teste de funcionamento:

	Acesse: localhost:8088


#####Referências:
  
>  1. http://hadoop.apache.org/docs/r2.5.0/hadoop-project-dist/hadoop-common/SingleCluster.html
>  2. https://wiki.archlinux.org/index.php/Hadoop
>  3. http://cute-jumper.github.io/linux/2014/09/05/install-hadoop-250-on-arch-linux/
>  4. Hadoop - the definitive guide. Tom white. 4ª Edição
>  5. http://chaalpritam.blogspot.com.br/2015/01/hadoop-260-single-node-cluster-setup-on.html

