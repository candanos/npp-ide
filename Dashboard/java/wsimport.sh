#!/bin/sh
export JAVA_HOME=/c/eclipse/ibm_sdk80

wsdlFile=/C/CodeRepos/scoretfs/loan-fx-notification-app/loan-fx-notification-web-v1/src/main/webapp/WEB-INF/wsdl/LoanFxNotificationServiceV1x3_PROD_Provider_WebService_Port1.wsdl

generationDir=/C/CodeRepos/scoretfs/loan-fx-notification-app/loan-fx-notification-client-v1/src/main/java/
bindingFile=/C/CodeRepos/scoretfs/loan-fx-notification-app/loan-fx-notification-web-v1/src/main/webapp/WEB-INF/wsdl/jaxws-binding.xml

$JAVA_HOME/bin/wsimport -Xnocompile -b $bindingFile -s $generationDir $wsdlFile 
read -p "Press enter ..."-+*