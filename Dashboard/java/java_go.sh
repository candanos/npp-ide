#!/bin/bash
echo $0
javafile=$2
PACKAGE="com.candanos"
JARLIB="/c/java/external-jars"
export JAVAFILEDIR=$(cygpath -u $(echo $1))
JAVAFILENAME=$2
JAVABASENAME=${JAVAFILENAME%.*}
cd ../..
export PRJDIR=$(pwd)

IDE_PATH="/c/npp-ide/Dashboard/java"
LLQ="Test"

os="UNIX"
if [[ "$(uname)" == "Linux" ]]; then
    echo "Linux system"
elif [[ "$(uname)" == *"CYGWIN"* ]]; then
    echo "Cygwin on Windows"
    os="WINDOWS"
elif [[ "$(uname)" == *"MINGW"* ]]; then
    echo "MinGW on Windows"
elif [[ "$(uname)" == "Darwin" ]]; then
    echo "MacOS system"
fi
export os
echo "hello1"
#
cat $JAVAFILEDIR/$JAVAFILENAME | grep "public static void main"; main=$?
echo "hello2"
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
export COMPILEENTRY="$PACKAGE.$COMPILEENTRY"
export TESTCLASS="$PACKAGE.$TESTCLASS"


# export JAVA_HOME="/c/Java/jdk1.8.0_261"
# export JAVA_HOME="/c/Java/jdk-11.0.11"
export JAVA_HOME="/c/java/jdk-17.0.9"
export PATH="$JAVA_HOME/bin":$IDE_PATH:$JARLIB:$PATH
 
#  
CLASSPATH=$PRJDIR:$JARLIB/*
SOURCEDIR=$PRJDIR
TARGETDIR=$PRJDIR
WINDOWS_CLASSPATH=$(cygpath -wp $(echo $CLASSPATH))
WINDOWS_SOURCEDIR=$(cygpath -w $(echo $SOURCEDIR))
WINDOWS_TARGETDIR=$(cygpath -w $(echo $TARGETDIR)) 
if [[ $os == "WINDOWS" ]]; then
    CLASSPATH=$WINDOWS_CLASSPATH
    SOURCEDIR=$WINDOWS_SOURCEDIR
    TARGETDIR=$WINDOWS_TARGETDIR
fi  
export CLASSPATH
export SOURCEDIR
export TARGETDIR
#
echo "compile"
. java_compile.sh
if [[ $java_compile -eq 0 ]]; then
    . java_run.sh
fi
echo "bye bye java_go"
read -p "Press [Enter] key to go on."