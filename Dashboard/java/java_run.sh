#!/bin/bash
vpn="java_run.sh"
echo "----------- $vpn  start .---------------------------------------"

#JUnit4
#JUnitCore is a facade for running tests.It supports running JUnit 4 tests, JUnit 3.8.x tests, and mixtures.
# testengine='org.junit.runner.JUnitCore'
# java -cp $CLASSPATH $testengine $JAVABASENAME

#JUnit5
# testengine='org.junit.platform.console.ConsoleLauncher'
# java -cp $CLASSPATH $testengine --class-path $CLASSPATH --select-class=$JAVABASENAME
#

if [[ $TYPE == "Main" ]]
then
    java -cp $CLASSPATH $JAVABASENAME -v
else
    testengine=$JARLIB'/junit-platform-console-standalone-1.9.0.jar'
    java -cp $CLASSPATH -jar $testengine --class-path $CLASSPATH --select-class=$TESTCLASS --disable-banner --details=flat #none, tree, flat, verbose
fi
echo "----------- $vpn  finish.---------------------------------------"
read -p "Press [Enter] key to go on."
# exit $java_run  #if you use as a seperate script instead of sourcing.