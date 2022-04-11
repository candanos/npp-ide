#!/bin/bash
pwd
java -version
javafile=$2
basename=${javafile%.*}
# echo $classname
echo "----------"
rm -fv *.class
echo "----------"
javac $javafile
echo "----------"
java $basename
echo "----------"
rm -fv *.class
echo "----------"
read -p "Press [Enter] key to go on."