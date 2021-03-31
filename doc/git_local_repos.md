# Introduction

This describes how to create and populate a repo on your local machine.

Also describes how to back up your repo (and restore it too).

# Create a "bare" repo

Make a directory for it, and init that directory to be a git repo.

```
cd ~/repos

mkdir XYZ.git
cd XYZ.git
git --bare init
```

Convert your dev directory to a local repo, and push it to the bare repo.

```
cd ~/dev/XYZ
git init
git add .
git commit -m "Initial checkin."
git remote add origin ~/repos/XYZ.git
git push -u origin master
```

# Backup strategy - bundle

Back up the "bare" repo as a bundle:
```
mkdir /media/whatever/repos_bundles

cd ~/repos/XYZ.git
git bundle create /media/whatever/repos_bundles/XYZ-all --all
```

Restore from bundle:

```
mkdir restore
cd restore
git clone /media/whatever/repos_bundles/XYZ-all XYZ.git
cd XYZ.git
git status
```

# Backup strategy - clone/mirror

Based on the theory that a clone mirror is a repo, just clone it.

```
mkdir /media/whatever/repos_mirrors
cd /media/whatever/repos_mirrors
git clone --mirror ~/repos/XYZ.git XYZ-mirror
```

Restore:

```
mkdir ~/repo_restore
cd ~/repo_restore
git clone /media/whatever/repos_mirrors/XYZ-mirror XYZ.git
```

# Backup strategty - just copy it

```
cp -r ~/repos/XYZ.git /media/whatever/repos_copy
```

To restore it, just copy it back:

```
mkdir ~/repo_restore
cp -r /media/whatever/repos_copy/XYZ.git ~/repo_restore
```

# References

https://stackoverflow.com/questions/7632454/how-do-you-use-git-bare-init-repository

https://stackoverflow.com/questions/1251713/backup-a-github-repository
