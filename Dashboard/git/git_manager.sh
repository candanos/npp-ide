#!/bin/bash

# git_manager.sh you can copy that file into your repository to handle git commands.
## user authorization and config 


## manage branches.
# This will create a new branch called 'NEW_BRANCH_NAME' and check it out.
# If no COMMIT_ID, then new branch is created from current branch.
("check out" means "to switch to the branch")
git checkout -b NEW_BRANCH_NAME COMMIT_ID 

# This just creates the new branch without checking it out.
git branch NEW_BRANCH_NAME COMMIT_ID

# remove a branch
git branch -d branch_name

# Delete the branch locally and forcefully if you have unmerged changes.
git branch -D $branch_name

# Delete the branch remotely (if needed)
git push origin --delete $branch_name

# delete commits 
