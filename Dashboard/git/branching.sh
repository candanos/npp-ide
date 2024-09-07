
# ("check out" means "to switch to the branch")
# This will create a new branch called 'NEW_BRANCH_NAME' and check it out. IF no COMMIT_ID then current branch.
git checkout -b NEW_BRANCH_NAME COMMIT_ID


# This just creates the new branch without checking it out.
git branch NEW_BRANCH_NAME COMMIT_ID

# This renames the current branch to new-branch-name
git branch -m new-branch-name