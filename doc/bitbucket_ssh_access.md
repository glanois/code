# How To Set Up SSH for BitBucket

This will enable you to automatically authenticate so you can do
things like `git clone git@bitbucket.org:myworkspace/myrepo.git`
without having to enter a username or password.

# Procedure

Go to your GL->Personal settings->SSH keys page, and click "generate an SSH key".
- https://bitbucket.org/account/settings/ssh-keys/

That will send you to https://support.atlassian.com/bitbucket-cloud/docs/set-up-an-ssh-key/

Scroll down to "Set up SSH on macOS/Linux".  Note that the instructions are slightly different
for macOS and Linux.
- Skip steps 1-2 if you already have a private key file ~/.ssh/id_rsa
- Step 3 is - cat your public key ~/.ssh/id_rsa.pub
  - `cat ~/.ssh/id_rsa.pub`

Go to your GL->Personal settings->SSH keys page, and click "Add key".
- https://bitbucket.org/account/settings/ssh-keys/

In the "Add key" dialog, give it a name (like "id_rsa.pub") and paste your
id_rsa.pub contents.  Click the "Add key" button.

This new key will show up in the list, and you'll get an email about it being added.

Do a command line test:

```
$ ssh -T git@bitbucket.org
```

Now you should be able to clone repos, eg:
```
git clone git@bitbucket.org:myworkspace/myrepo.git
```

