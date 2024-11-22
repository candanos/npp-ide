#!/bin/bash 
git diff dev:COPY/PPINSRPR.cpy int:COPY/PPINSRPR.cpy
git diff 3cd1e0f:kola-ui-dc/src/main/resources/config/localdev/KolaProperties.properties HEAD:kola-ui-dc/src/main/resources/config/localdev/KolaProperties.properties
git diff HEAD^ HEAD

#compare master and origin  
git diff master origin/master

#As of Git 1.8.5, @ is an alias for HEAD, so you can use:

git diff @~..@

#The following will also work:

git show

#If you want to know the diff between head and any commit you can use:

git diff commit_id HEAD

#And this will launch your visual diff tool (if configured):

git difftool HEAD^ HEAD

#Since comparison to HEAD is default you can omit it (as pointed out by Orient):

git diff @^
git diff HEAD^
git diff commit_id

#
git log --name-only 
git log --name-only --oneline
git diff --name-only SHA1 SHA2
git diff --name-only HEAD~10 HEAD~5
git diff --name-only HEAD~1 HEAD

git diff branch_name --name-only # diff between your previous commit and working_directory
git diff commit_id --name-only # diff between a commit and working_directory
git diff file_path # diff between the file in working directory and previous commit

# compare states of repositories in different folders
git diff --name-only /path/to/first/repo /path/to/second/repo

