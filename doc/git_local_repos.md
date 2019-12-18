# Local Repos

1. Create the "bare" repo:

   ```
   cd ~/repos

   mkdir XYZ.git
   cd XYZ.git
   git --bare init
   ```

1. Convert a directory to a local repo, and push it to the bare repo:

   ```
   cd ~/dev/XYZ
   git init
   git add .
   git commit -m "Initial checkin."
   git remote add origin ~/repos/XYZ.git
   git push -u origin master
   ```

1. Back up the "bare" repo:

   ```
   mkdir /media/whatever/repos_bundles

   cd ~/repos/XYZ.git
   git bundle create /media/whatever/repos_bundles/XYZ-all --all
   ```

1. Restore from bundle

   ```
   mkdir restore
   cd restore
   git clone /media/whatever/repos_bundles/XYZ-all XYZ
   cd XYZ
   git status
   ```

# References

https://stackoverflow.com/questions/7632454/how-do-you-use-git-bare-init-repository
