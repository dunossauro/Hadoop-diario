#!/bin/bash
clear
echo -e "
##################################################################
##\t\tBem vindo a instalação do Apache Hadoop 2.7\t##
##################################################################
\n\n"

INSTALL_LOCAL=/usr/local/
HADOOP_ETC=/usr/local/hadoop/etc/hadoop

download(){
  wget http://mirror.nbtelecom.com.br/apache/hadoop/common/hadoop-2.7.1/hadoop-2.7.1.tar.gz
  tar xvvf hadoop-*.tar.gz
  sudo mv hadoop-* $INSTALL_LOCAL
}

inicio(){
  echo -e "Desja efetuar do Download? (S/N)"
  read bool

  case $bool in
    "s"|"S" ) download ;;
    "n"|"N") ;;
    * ) echo -e "Digite uma opção válida"
        inicio ;;
  esac
}

modo_de_instalacao(){
  echo -e "\n\nDigite o modo de instalação:\n\n\
  1 - Standalone\n\
  2 - Pseudo-distributed\n\
  3 - Cluster-mode\n"

  read mode

  case $mode in
    1 )

        echo -e "Digite o caminho de instalação do seu java EX: /usr/lib/jvm/default"
        read CAMINHO_JAVA
        echo -e "export JAVA_HOME=$CAMINHO_JAVA" >> hadoop-env.sh
        sudo mv hadoop-env.sh $HADOOP_ETC
        clear
        echo "Modo Standalone instalado om sucesso!!!"
      ;;
    2 )
        echo -e "Digite o caminho de instalação do seu java EX: /usr/lib/jvm/default"
        read CAMINHO_JAVA
        echo -e "export JAVA_HOME=$CAMINHO_JAVA" >> hadoop-env.sh
        sudo mv hadoop-env.sh $HADOOP_ETC
        sudo mv p_core-site.xml $HADOOP_ETC
        sudo mv p_mapred-site.xml $HADOOP_ETC
        sudo mv p_yarn-site.xml $HADOOP_ETC
        sudo mv p_hdfs-site.xml $HADOOP_ETC
        clear
        echo "Modo Pseudo-distributed instalado om sucesso!!!"
      ;;
    3 )
      ;;
    * ) echo -e "Digite uma opção válida"
        modo_de_instalacao;;
  esac
}

inicio
modo_de_instalacao
