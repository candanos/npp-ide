#!/bin/bash
export NODEJS_PATH='/c/nodejs'
echo $NODEJS_PATH
echo $PATH
export PATH=$NODEJS_PATH:$PATH
echo $PATH
cd '/c/npm'
pwd
npm install mermaid