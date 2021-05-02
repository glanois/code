# References

https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/connecting-to-github-with-ssh

# Converting Existing http-based Clone To Use SSH

If you cloned originally using an HTTP URL you are going to have to convert it over use your username before you cane use command-line SSH authentication for `push` and other such Git commands.

See https://stackoverflow.com/questions/23546865/how-to-configure-command-line-git-to-use-ssh-key

See accepted answer:

Assuming that you have used ssh-keygen to generate a key pair and uploaded the public key in the appropriate place in your github account, you should be able to set remote to use the url `git@github.com:username/repo.git`.

```
git remote set-url origin git@github.com:username/repo.git
```

If you do not have local changes that you care about, you can just delete your local repository and clone again:

```
git clone git@github.com:username/repo.git
```
