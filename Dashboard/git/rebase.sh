# How can I merge my two consequtive bugfix commits into a single one in git ? 

git rebase -i HEAD~2 #that opens an interactive editor. 

pick abc1234 First bugfix
pick def5678 Second bugfix
# Edit the commits: In the editor, change the second commit (def5678 in this example) from pick to squash (or s):
pick abc1234 First bugfix
squash def5678 Second bugfix


# squash means merge with the previous commit in the commit ID of the latest.

# Save and close the editor: After saving and closing, Git will squash the second commit into the first.

# Edit the commit message: Git will then open another editor to let you modify the commit message. You can combine the two commit messages or write a new one entirely.

# Finish the rebase: Save and close the editor again, and Git will finish the rebase, leaving you with a single commit that combines the changes from both.

# Now your two bugfix commits are merged into one!
