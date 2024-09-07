#!/bin/bash
vpn="java_compile.sh"
echo "----------- $vpn  start .---------------------------------------"
cd $JAVAFILEDIR
rm -fv $COMPILEENTRY*.class
# javac -d " + targetpath + " -sourcepath "  + sourcepath + " -cp  " + classpath + " " + javaFileName
# javac -verbose -cp $CLASSPATH $JAVAFILENAME 2>&1 | grep "Test.class"

javac -verbose -cp $CLASSPATH $COMPILEENTRY'.java' 2>&1 | grep "wrote\|error" #javac commands go to stderr by default so you must redirect 2 to 1 (stderr to stdout) 
#javac -cp $CLASSPATH $JAVAFILENAME
java_compile=${PIPESTATUS[0]}
echo "Exit code is: " $java_compile
echo "----------- $vpn  finish.---------------------------------------"
# read -p "Press [Enter] key to go on."
# exit $java_compile  #if you use as a seperate script instead of sourcing.