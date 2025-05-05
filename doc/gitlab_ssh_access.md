# GitLab SSH Access

https://docs.gitlab.com/ee/ssh/index.html#generate-an-ssh-key-pair

```
ssh-keygen -t ed25519 -C "hangar21"
```

```
cat ~/.ssh/id_ed25519.pub
```

Go to User Settings -> SSH Keys
Paste into page, click "Add key"

```
git clone git@gitlab.com:iswteam/swbuild.git
cd bld
make PYTHON=python3 CPPSTD=c++17
```

## 