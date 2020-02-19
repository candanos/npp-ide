#!/bin/bash 
cd "c:/CodeRepos/scoretfs/fx-loan-notification-api"
git checkout develop
git add .
git commit -m "BugFix"
git push 
cd "c:/CodeRepos/scoretfs/loan-fx-notification-batch"
git checkout develop
git add .
git commit -m "BugFix"
git push
cd "c:/CodeRepos/scoretfs/loan-fx-notification-app"
git checkout develop
git add .
git commit -m "BugFix"
git push