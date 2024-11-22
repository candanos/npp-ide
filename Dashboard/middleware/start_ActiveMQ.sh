#!/bin/bash
 
activeMQ_Home="C:\java\middleware\apache-activemq-6.1.3"
activeMQ_Home=$(cygpath -u $(echo $activeMQ_Home))
echo $activeMQ_Home
cd $activeMQ_Home"/bin"
JAVA_HOME="C:\java\jdk-17.0.9"
export JAVA_HOME=$(cygpath -u $(echo $JAVA_HOME))
export PATH="$JAVA_HOME/bin":$PATH

./activemq 'start'

