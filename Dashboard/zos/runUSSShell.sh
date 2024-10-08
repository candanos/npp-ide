#!/bin/bash
# echo $mvs
# echo $uss
# echo $heredoc
# ssh -tt -o "BatchMode yes" cy59857@sman.isbank  <<HERE
# cp "//'$mvs'" $uss                  
# HERE

# ssh -tt -o "BatchMode yes" xlrint1@sman.isbank  <<HERE
# cob2 -c -I/u/ttg/ebcdicRepos/isbank-cobol-framework/COBOL:/u/ttg/ebcdicRepos/isbank-cobol-framework/COPY -v /u/ttg/ebcdicRepos/isbank-cobol-framework/COBOL/TARIHPGM.cbl 
# HERE


options='LIB,SSR,SIZE(MAX),BUF(32760),XREF(SHORT),NOC(E),NOSEQ,F(W),RENT,TERM,ARITH(EXTEND),OPT(FULL),SQL,CODEPAGE(1026)'
dir='/u/ttg/compileSets/mainframe-all-apps/prd/C0001'
members='ALCEKOZT.cbl'
# sh /u/ttg/cob2Compiler.sh "$members" "$dir" "$options"
ssh -tt -o "BatchMode yes" xlrint1@sman.isbank  <<HERE
rm -rf /u/ttg/buildSets/mainframe-all-apps/prd/C0003/log
exit
HERE
read -p "Press [Enter] key to go on." 

# git config --global credential.helper store --file=/u/ttg/meZgit/.credentials
# mkdir /u/ttg/tfsRepos/core-banking-app/COPY
# mkdir /u/ttg/tfsRepos/core-banking-api/COBOL
# mkdir /u/ttg/tfsRepos/core-banking-api/COPY
# mkdir /u/ttg/tfsRepos/isbank-cobol-framework/COBOL
# mkdir /u/ttg/tfsRepos/isbank-cobol-framework/COPY
# mkdir /u/ttg/tfsRepos/kredi-kartlari-app/COBOL
# mkdir /u/ttg/tfsRepos/kredi-kartlari-app/COPY
# mkdir /u/ttg/tfsRepos/kredi-kartlari-api/COBOL
# mkdir /u/ttg/tfsRepos/kredi-kartlari-api/COPY
# mkdir /u/ttg/tfsRepos/payments-swift-api/COBOL
# mkdir /u/ttg/tfsRepos/payments-swift-api/COPY 
# mkdir /u/ttg/tfsRepos/payments-swift-app/COBOL
# mkdir /u/ttg/tfsRepos/payments-swift-app/COPY
# mkdir /u/ttg/tfsRepos/others-api/COBOL
# mkdir /u/ttg/tfsRepos/others-api/COPY
# mkdir /u/ttg/tfsRepos/others-app/COBOL
# mkdir /u/ttg/tfsRepos/others-app/COPY
# mkdir /u/ttg/tfsRepos/menkul-kiymetler-app/COBOL
# mkdir /u/ttg/tfsRepos/menkul-kiymetler-app/COPY
# mkdir /u/ttg/tfsRepos/menkul-kiymetler-api/COBOL
# mkdir /u/ttg/tfsRepos/menkul-kiymetler-api/COPY