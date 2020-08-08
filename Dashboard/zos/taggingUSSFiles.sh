#!/bin/bash
# echo $mvs
# echo $uss
# echo $heredoc
# ssh -tt -o "BatchMode yes" cy59857@sman.isbank  <<HERE
# cp "//'$mvs'" $uss                  
# HERE
ssh -tt -o "BatchMode yes" xlrint1@sman.isbank  <<HERE
cob2 -c 
HERE
read -p "Press [Enter] key to go on." 