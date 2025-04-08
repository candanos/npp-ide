#!/bin/bash
vpn="java_compile.sh"
echo "----------- $vpn  start .---------------------------------------"
cd $JAVAFILEDIR
rm -fv $COMPILEENTRY*.class
# rm -fv *.class
echo $COMPILEENTRY
# javac -d " + targetpath + " -sourcepath "  + sourcepath + " -cp  " + classpath + " " + javaFileName
# javac -verbose -cp $CLASSPATH $JAVAFILENAME 2>&1 | grep "Test.class"
echo "TARGETDIR:"$TARGETDIR
echo "SOURCEDIR:"$SOURCEDIR
echo "CLASSPATH:"$CLASSPATH
# javac -verbose -d $TARGETDIR -sourcepath $SOURCEDIR -classpath $CLASSPATH $COMPILEENTRY'.java' 2>&1 | grep "wrote\|error" #javac commands go to stderr by default so you must redirect 2 to 1 (stderr to stdout) 
#   open the following command for more detailed debug.
# javac -d $targetpath -sourcepath $SOURCEPATH -cp $CLASSPATH $JAVAFILENAME  
cd $PRJDIR
pwd
# javac -cp $WINDOWS_CLASSPATH -processor lombok.launch.AnnotationProcessorHider\$AnnotationProcessor "com/candanos/"$JAVAFILENAME
javac -cp $WINDOWS_CLASSPATH "com/candanos/"$JAVAFILENAME 
# javac -cp $WINDOWS_CLASSPATH -processor lombok.launch.AnnotationProcessor "com/candanos/"$JAVAFILENAME

java_compile=${PIPESTATUS[0]}
echo "Exit code is: " $java_compile
echo "----------- $vpn  finish.---------------------------------------"
# read -p "Press [Enter] key to go on."
# exit $java_compile  #if you use as a seperate script instead of sourcing.