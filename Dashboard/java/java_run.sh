#!/bin/bash
vpn="java_run.sh"
echo "----------- $vpn  start .---------------------------------------"
cd $PRJDIR
echo "COMPILEENTRY:"$COMPILEENTRY
#JUnit4
#JUnitCore is a facade for running tests.It supports running JUnit 4 tests, JUnit 3.8.x tests, and mixtures.
# testengine='org.junit.runner.JUnitCore'
# java -cp $CLASSPATH $testengine $JAVABASENAME

#JUnit5
# testengine='org.junit.platform.console.ConsoleLauncher'
# java -cp $CLASSPATH $testengine --class-path $CLASSPATH --select-class=$JAVABASENAME
#

CONFIG=$JAVAFILEDIR/application.yml
SPRING_CONFIG=$(cygpath -w $(echo $CONFIG)) 
echo $SPRING_CONFIG

if [[ $TYPE == "Main" ]]
then
    # java -cp $CLASSPATH $JAVABASENAME -v
    java -cp $WINDOWS_CLASSPATH  -Dspring.config.location=file:$SPRING_CONFIG $COMPILEENTRY -v
else
    testengine=$JARLIB'/junit-platform-console-standalone-1.9.0.jar'
    java -cp $CP -jar $testengine --class-path $CP --select-class=$TESTCLASS --disable-banner --details=flat #none, tree, flat, verbose
fi
echo "----------- $vpn  finish.---------------------------------------"
# read -p "Press [Enter] key to go on."
# exit $java_run  #if you use as a seperate script instead of sourcing.