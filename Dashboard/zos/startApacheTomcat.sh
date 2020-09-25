#!/bin/bash
ssh -tt -o "BatchMode yes" xlrint1@sman.isbank  <<HERE
sh "/u/ttg/apache-tomcat-9.0.36/bin/startup.sh"
exit
HERE
read -p "Press [Enter] key to go on." 