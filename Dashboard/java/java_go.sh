#!/bin/bash
echo $0
javafiledir=$1
javafile=$2
JAVAFILENAME=$javafile
JAVABASENAME=${javafile%.*}
JAVAFILEDIR=$javafiledir
JARLIB="/c/Java/externalJars"
IDE_PATH="/c/npp-ide/Dashboard/java"
LLQ="Test"
# JAVABASENAME Ctrl+Shift+E file name can be Car or CarTest (Car+LLQ) 
#
echo $JAVAFILENAME
cat $JAVAFILEDIR'\'$JAVAFILENAME | grep "public static void main"; main=$?

if [[ $main -eq 0 ]]
then
    TYPE="Main"
    COMPILEENTRY=$JAVABASENAME
elif [[ $JAVABASENAME == *$LLQ ]]
then 
    COMPILEENTRY=$JAVABASENAME
    TESTCLASS=$JAVABASENAME
else
    COMPILEENTRY=$JAVABASENAME$LLQ
    TESTCLASS=$JAVABASENAME$LLQ
fi

# setting java environment variables
    # export PATH=/usr/local/mysql/bin:$PATH
    # export CLASSPATH=.:/c/Java/externalJars/ejb.jar
export JAVA_HOME="/c/Java/jdk1.8.0_261"
export JAVA_HOME="/c/Java/jdk-11.0.11"
export PATH="$JAVA_HOME/bin":$IDE_PATH:$JARLIB:$PATH
# java -version 

# Adding jars in the directory to the classpath
jars='.' # derlenecek class in kendi directorysini burada ekliyor.
cd $JARLIB
for mbr in *
do
	jars=$jars:$JARLIB/$mbr
done
export CLASSPATH=$jars

. java_compile.sh
if [[ $java_compile -eq 0 ]]; then
    . java_run.sh
fi
echo "bye bye java_go"
read -p "Press [Enter] key to go on."