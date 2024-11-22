#!/bin/bash

JAVA_HOME="/c/java/jdk-17.0.9"
JAVA_HOME_WINDOWS=$(cygpath -w $(echo $JAVA_HOME))
echo "unix to windows:"$JAVA_HOME">>"$JAVA_HOME_WINDOWS
winpath="C:\java\middleware\cygwin\apache-activemq-6.1.3-bin.tar.gz"
unixpath=$(cygpath -u $(echo $winpath))
echo "windows to unix:"$winpath">>"$unixpath


