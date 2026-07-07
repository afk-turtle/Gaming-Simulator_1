Basic Git commands

######################################################################################################
The typical GitHub workflow order is:

Check what changed
Add files to staging
Commit changes
Push commit to GitHub

The basic command order is:

git status
git add .
git commit -m "Describe what you changed"
git push

######################################################################################################
(no need to do git push origin main if...) 
If already used -u (or --set-upstream) when pushing a branch for the first time, no need to specify origin main every time.

For example, the first time when pushing:

git push -u origin main

This does two things:

Pushes your local main branch to GitHub's origin/main
Sets the upstream tracking relationship:
Local main  →  origin/main

After that, you can simply use:

git push

Git already knows:

which remote (origin)
which branch (main)
Example workflow

First time:

git add .
git commit -m "Initial project setup"
git push -u origin main

Future pushes:

git add .
git commit -m "Added login feature"
git push