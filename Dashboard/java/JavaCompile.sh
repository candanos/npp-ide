#!/bin/bash

javafiledir=$1
javafile=$2
# export PATH=/usr/local/mysql/bin:$PATH
# export CLASSPATH=.:/c/Java/externalJars/ejb.jar

# setting java environment variables
export JAVA_HOME="/c/Java/jdk-11.0.11"
export JAVA_HOME="/c/Java/jdk1.8.0_261"
export PATH="$JAVA_HOME/bin":$PATH
java -version 
echo 'PATH='$PATH

# Adding jars in a directory to the classpath
LIB="/c/Java/externalJars"
jars='.'
cd $LIB
for mbr in *
do
	jars=$jars:$LIB/$mbr
done
echo 'CLASSPATH='$jars


cd "$javafiledir"
basename=${javafile%.*}

# echo $classname
echo "----------"
rm -fv *.class
echo "---javac started---"
javac -cp $jars $javafile
echo "---javac ended---"
java -cp $jars $basename
echo "----------"
# rm -fv *.class
echo "----------"
read -p "Press [Enter] key to go on."