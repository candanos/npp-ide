#!/bin/bash
pwd
x=$(cygpath -w $(pwd))
echo $x
CERTFILE=$(cygpath -w $(echo $JAVA_HOME"/lib/security/cacerts"))
echo $CERTFILE