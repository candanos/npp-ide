#!/bin/bash
# testengine='/c/Java/externalJars/junit-platform-console-standalone-1.9.0.jar'
# java -jar $testengine

JAVABASENAME="S02BubbleSortTest"
llq="Test"
if [[ $JAVABASENAME = *$llq ]]
then 
    CLASSNAME=${JAVABASENAME%$llq}
else
    CLASSNAME=$JAVABASENAME$llq
fi 
echo $CLASSNAME
read -p "Press [Enter] key to go on."