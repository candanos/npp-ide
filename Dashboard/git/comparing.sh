#!/bin/bash 
git diff HEAD^ HEAD

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

