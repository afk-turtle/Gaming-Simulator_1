Basic Git commands
(This includes basic commands, usage of set-upstream, and erase the commit before pushing if needed)

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

* You can check your last commits with:
git log --oneline

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


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
If you want to erase the commit before pushing

You have a few options.

1. Undo the commit but keep your changes (most common)
git reset --soft HEAD~1

This removes the commit but keeps your files changed and staged.

2. Undo the commit and unstage the changes
git reset HEAD~1

Your files stay modified, but they are no longer staged.

You can check:

git status
3. Completely delete the commit and changes

⚠️ This permanently removes the work:

git reset --hard HEAD~1

- If you already pushed the commit 
Then it is different. The commit is on GitHub, so removing it requires rewriting history:

git reset --hard HEAD~1
git push --force

This should be used carefully, especially on shared repositories.

* You can check your last commits with:
git log --oneline