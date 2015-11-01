#Configuração do modo totalmente distribuído

Para configurar o modo totalmente distribuído você deve cofigurar o modo pseudo-distribuído anteriormente:

    https://github.com/z4r4tu5tr4/Hadoop-diario/blob/master/Pseudo-Distributed-Mode/readme.md
    
Existem poucas diferenças entre a configuração do pseudo-distribuído e o modo completamente distribuído. Na verdade, o Hadoop só precisa estar instalado em todos os nós do nosso cluster e podemos fazer isso de uma maneira muito simples:

    rsync -avxP /usr/local/hadoop root@<ip_do_cliente>:/usr/local/hadoop

Mas para que isso aconteça de uma maneira transparente temos que configurar o SSH do server, para autenticação sem senha, em todos os outros nós que farão parte do nosso cluster.

(Configuração do SSH)

Os arquivos XML tem algumas pequenas modificações

core-site.xml:
aqui definimos o uso do HDFS e o endereço do seu master e a porta que será usada

	<?xml version="1.0" encoding="UTF-8"?>
	<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

	<configuration>
		<property>
			<name>fs.defaultFS</name>
			<value>hdfs://NOME_DO_SEU_MASTER:9000</value>
		</property>
	</configuration>

hdfs-site.xml:
Aqui está sendo definido o numero de replicações de cada arquivo do HDFS

	<?xml version="1.0" encoding="UTF-8"?>
	<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

	<configuration>
   		<property>
      			<name>dfs.replication</name>
      			<value>3</value>
   		</property>
	</configuration>

mapred-site.xml:
Aqui passamos a bola do gerenciador de MapReduce para o Yarn e dizemos quem vai ser o Master para distribuir tarefas
	
	<?xml version="1.0"?>
	<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

	<configuration>
   		<property>
      			<name>mapred.job.tracker</name>
      			<value>NOME_DO_SEU_MASTER:5431</value>
   		</property>
   		<property>
      			<name>mapred.framework.name</name>
      			<value>yarn</value>	
   		</property>
	</configuration>

yarn-site.xml:

	<?xml version="1.0"?>

	<configuration>
		<property>
    			<name>yarn.resourcemanager.resource-tracker.address</name>
        		<value>NOME_DO_SEU_MASTER:8025</value>
    		</property>
    		<property>
    			<name>yarn.resourcemanager.scheduler.address</name>
        		<value>NOME_DO_SEU_MASTER:8035</value>
   		</property>
    		<property>
    			<name>yarn.resourcemanager.address</name>
        		<value>NOME_DO_SEU_MASTER:8050</value>
    		</property>
</configuration>
Todos os outros nós precisam estar nomeados no seu /etc/hosts

	hadoopmaster	<IP>
	hadoopslave1	<IP>
	hadoopslave2	<IP>
	hadoopslave3	<IP>
	hadoopslave4	<IP>
	hadoopslave5	<IP>
	hadoopslave6	<IP>
	hadoopslave7	<IP>
	hadoopslave8	<IP>
	hadoopslave9	<IP>

Agora, dois novos arquivos precisam ser criados dentro de /usr/local/hadoop/etc/hadoop

	slaves:
	
		hadoopslave1
		hadoopslave2
		hadoopslave3
		hadoopslave4
		hadoopslave5
		hadoopslave6
		hadoopslave7
		hadoopslave8
		hadoopslave9

	master:

		hadoopmaster


##Teste de funcionamento:

	Acesse: localhost:8088


#####Referências:
  
>  1. http://hadoop.apache.org/docs/r2.5.0/hadoop-project-dist/hadoop-common/SingleCluster.html
>  2. https://wiki.archlinux.org/index.php/Hadoop
>  3. http://cute-jumper.github.io/linux/2014/09/05/install-hadoop-250-on-arch-linux/
>  4. Hadoop - the definitive guide. Tom white. 4ª Edição
>  5. http://chaalpritam.blogspot.com.br/2015/01/hadoop-260-single-node-cluster-setup-on.html
