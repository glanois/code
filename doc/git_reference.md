# RESOURCES

https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging

# CONFIGURATION

## Windows Secure Channel Library

https://stackoverflow.com/questions/45742607/switch-to-native-windows-secure-channel-library-from-openssl-library-on-wind

## What is my configuration and where does it fome from?

https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup

`git config --list --show origin`

## Flag as untracked a file when its case changes

`git config core.ignorecase false`

## Use Windows Credential Manager

https://support.microsoft.com/en-us/windows/accessing-credential-manager-1b5c916a-6a16-889f-8581-fc16e8165ac0

## Email and user name configuration

```
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

# REPOSITORY

## Clone a repository (default repo name)

This will cone to a folder whose name is given in the URL ending in .git.

`git clone <url>`

## Clone a repository (to a specific folder)

`git clone <url> <folder>`

## Clone a specific branch of a repository

`git clone <url> -b <branchname> --single-branch <folder>`

# BRANCH

## What branch am I on, and what ones are available

`git branch -v -a`

## Switch to an existing branch

`git checkout <branchname>`

## Checkout an existing remote branch

`git checkout -b <branchname> origin/<branchname`

## Create a new branch and put me on it

Beware that the new branch will be created as a sub-branch of the branch you are currently on at the time you issue the command.

If you want the new branch to be a branch off of master, be sure to switch to the master branch first (`git checkout master`) before creating the sub-branch.

`git checkout -b <sub-branchname>`

Equivalent to:
```
git branch <sub-branchname>
git checkout <sub-branchname>
```

## Create a sub-branch of a branch

`git checkout -b <sub-branch> <currentbranch>`

## Show branch hierarchy

`git show-branch`

## Update local list of remote branches

`git remote update origin --prune`

## Rename a local and remote branch

```
git checkout <oldname>
git branch -m <newname>
git push -u origin <newname>
git push origin --delete <oldname>
```

## Delete remote and local branch

```
git push --delete <remote_name> <branchname>
git branch --delete <branchname>
```

You'll be warned about unmerged local changes; use `-D` instead.

You'll be warnted about the branch not being fully merged; use `-D` instead.

## Delete remote tracking reference

`git branch -d -r origin/<branchname>`

## Update master after pull request is merged

After your pull request is merged, use this to update your local copy of master.

```
git checkout master
git pull
```

`pull` is a `fetch` and a `merge` so you could do it in steps:

```
git checkout master
git fetch
git diff master..origin/master
git diff --name-only master..origin/master
git merge
```

## Update your feature branch (which is a branch off master) with master

```
git checkout master
git fetch -p origin
git merge origin/master
git checkout <branch_name>
git merge master
git push origin <branch_name>
```

Alternatively, you can do a rebase:

```
git fetch
git rebase origin/master
```

## Merge a commit from another branch

1. In source branch, do a `git log` and shop the SHA hash of the commit.

1. Checkout the destination branch, then...

`git cherry-pick <hash key>`

Then push it.

## Merge all commits from another branch

First, find the first and last commits from that branch:

`git log --oneline`

Then cherry pick the range.  (Remember to add the '^' to make it inclusive.)

`git cherry-pick <first commit>^..<lastcommit>`

# STAGE

## Status of all files - modified, new, untracked, deleted

`git status`

## Stage all new and modified files

`git add --all`

or

`git add -A`

## Stage all modified files (but ignore untracked files)

`git add -u`

## Interactively stage files

`git add --interactive`

or

`git add -i`

## Stage new files and modifications, without deletions

`git add .`

## Compare staged file to previous revision

`git diff --cached <file>`

## What files are staged

Note that `git status` has more/better information.

`git diff --name-only --cached`

## Unmodify/undelete a file you modified or deleted prior to committing

`git checkout -- <file>`

## Remove a staged file you staged previously with `git add`

`git reset <file>`

## List all untracked files

`git ls-files -o --exclude-standard`

Null-separate filenames and do something with them:

`git ls-files -z -o --exclude-standard | xargs -0 -I {} cmd {}`

# STASH

## Stash all pending work

`git stash push` (or just `git stash`)

## List stashes

`git stash list`

## Show the files in the stash

`git stash show`

## Show the changes in each file in the stash

`git stash show -p`

## Apply the changes in the stash (and keep the stash)

`git stash apply`

## Create a new branch with the changes in the stash

`git stash branch <branchname>`

## Apply the changes in the stash (and remove the stash)

`git stash pop`

# SQUASH

Squash the last n commits - https://forum.freecodecamp.org/t/how-to-squash-multiple-commits-into-one-with-git-squash/13231

`git rebase -i HEAD~n`

Leave the first commit as `pick`, change the rest to `squash`.

Then `git push -f` if you already pushed the n commits previously.

# COMMIT / PUSH / PULL

## Commit staged files

`git commit -m "<comment>"`

## Push branch to remote repository

Subsequent pushed don't need the `-u origin <branch>`, you can just `git push`.

`git push -u origin <branch>`

## Update your local branch with latest from remote

`git pull origin <branch>`

## List pending commits

`git log --branches --not --remotes`

# REVERT

## Revert changes to a file back to last commit

`git status` will remind you how to do this.

`git checkout -- <file>`

# HISTORY

## History of commits to a file

`git log --follow -- <file>`

`git log --oneline --pretty=format:"%h%x09%an%ad%x09%s" <filename>`

## Identify the developer for each line of code in a file

`git blame <filename>`

## History of all branches, commits, and merges to a repo

`git log --all --decorate --oneline --graph`

## History of a particular branch in a repo

`git log --decorate --oneline --graph <branch>`

## Show most recent revision of a file

`git show HEAD:./<filename`

# RENAME

## Rename a file

`git mv <filename>`

# DELETE

## Delete a file

`git rm <filename>`

## Delete a directory

`git rm -r <directory>`

## Deleting a clone

If you get permission errors deleting a clone, such as:

```
$ rm -rf myclone 
.
.
.
rm: myclone/.git/objects/fb/15c0ea4797c8fd3c3f11feb868405c6efb4d4a: Operation not permitted
rm: myclone/.git/objects/fb/eb8e3b7a5ed670c73be41c664f90102b4ab6f8: Operation not permitted
rm: myclone/.git/objects/fb: Directory not empty
rm: myclone/.git/objects: Directory not empty
rm: myclone/.git: Directory not empty
rm: myclone: Directory not empty
```

Normally you'd `ls -la` and `chmod` to fix this.  If that doesn't work,
chances are the `uchg` (immutable) flag has been set.  You can unset that with:

```
$ chflags -R nouchg ./myclone
```

Then you should be able to `rm -rf` it.

# PULL REQUEST

## Delete a pulll request

First, make a backup of any changes you might want to preserve, say for a second attempt.

https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/closing-a-pull-request

There will be a `Delete Branch` button.  Use it.

# DIFF / MERGE

## List all merge conflicts

`git diff --name-only --diff-filter=U`

## Comparing

### Command Line

|Description|Command|
|-----------|-------|
Compare two branches|`git diff <branch1>..<branch2>`
Compare two branches - file names only|`git diff --name-only <branch1>..<branch2>`
Compare two files on different branches|`git diff <branch1> <branch2> -- <filename>`
Compare `HEAD` revision on current branch to other branch|`git diff HEAD <branch2> -- <filename>`

### GitHub

Add `/compare` to your repo URL, and use the dropdown menus to select the branches to compare.

https://docs.github.com/en/github/committing-changes-to-your-project/comparing-commits

## Use a specific diff tool

`git difftool --extcmd=diff --no-prompt <file>`

## Another way to use a specific diff tool

https://coderwall.com/p/76wmzq/winmerge-as-git-difftool-on-windows

Put this in your .gitconfig (C:/Users/<username>/.gitconfig):

```
[diff]
    tool = winmerge
[difftool "winmerge"]
    cmd = "'C:/Program Files/WinMerge/WinMergeU.exe'" -e "$LOCAL" "$REMOTE"
```

Now you can invoke it from the command line:

`git difftool --no-prompt <file>`
`git difftool --no-prompt .`
`git difftool --no-prompt HEAD..67de2065`

## You can set up git to use a specific merge tool

https://stackoverflow.com/questions/2468230/how-to-use-winmerge-with-git-extensions

# GITHUB

## Add issues to a fork

Go into your fork, click `Settings`, go to the `Features` section, and set the `Issues` checkbox.
