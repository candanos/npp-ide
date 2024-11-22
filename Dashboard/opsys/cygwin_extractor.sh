#!/bin/bash
winpath="C:\java\middleware\cygwin\apache-activemq-6.1.3-bin.tar.gz"
unixpath=$(cygpath -u $(echo $winpath))
echo $unixpath
tar -xvzf $unixpath