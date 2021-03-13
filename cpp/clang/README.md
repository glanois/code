# INTRODUCTION

As a C++ developer who uses an Apple Macintosh computer running Mac OSX,
you will eventually be prevented from upgrading your operating system
at Apple's whim.  And coupled with that, upgrading Xcode will require
upgrading the operating system.

To get around this problem, you can install Clang yourself directly.

This article describes two ways to install Clang - via the Homebrew package manager, or via a pre-built binary distribution from llvm.org.

## Option 1 - Install Clang from Homebrew

https://brew.sh

### Install Hombrew

Ref: https://embeddedartistry.com/blog/2017/02/24/installing-llvm-clang-on-osx/

```
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Install LLVM

Nominally you can just do a `brew install llvm`, but that will fail on older
versions of MacOS X as the Homebrew team end-of-lifes them.

The message you will get will be that the "bottle" (binary distribution)
doesn't exist; you will need to build/install from source.  The messsage
will contain the command you need (`brew install --build-from-source <package>`).

```
$ brew install llvm
```

Just keep trying `brew install --build-from-source llvm` to find & build all
the dependencies.  Eventually llvm will build (takes a long time - mine was 106
minutes).

```
$ brew install --build-from-source gdbm
$ brew install --build-from-source mpdecimal
$ brew install --build-from-source openssl@1.1
$ brew install --build-from-source readline
$ brew install --build-from-source sqlite
$ brew install --build-from-source tcl-tk
$ brew install --build-from-source python@3.9
$ brew install --build-from-source sphinx-doc
$ brew install --build-from-source cmake
$ brew install --build-from-source libffi
$ brew install --build-from-source llvm
```

### Test it

$ brew info llvm

This gives very important suggestions about setting environment variables
to get it to work.

Now look where llvm got installed:

```
brew --prefix llvm
```

Probably `/usr/local/opt/llvm/bin`.  

Ask what version you got:

```
/usr/local/opt/llvm/bin/clang++ --version
```

In your `.bash_profile`, add this directory:
```
export PATH="/usr/local/opt/llvm/bin:$PATH"
```


## Option 2 - Install Clang from llvm.org

This is a simpler, faster way to get Clang.

### Download the binary

Go to the download page, pre-built binaries section, click macOS.

https://releases.llvm.org/download.html

For example:
```
clang+llvm-11.0.0-x86_64-apple-darwin.tar.xz
```

### Un-tar the binary

Use this to un-tar:

```
$ tar -xJvf clang+llvm-11.0.0-x86_64-apple-darwin.tar.xz
```

### Try it

```
$ ../../dev-tools/clang+llvm-11.0.0-x86_64-apple-darwin/bin/clang++ --std=c++17 c17.cpp 
ld: unknown option: -platform_version
clang-11: error: linker command failed with exit code 1 (use -v to see invocation)
```

That error is a problem.

### Fix the problem

Use `-verbose` switch to find what linker you are invoking.  Probably `/usr/bin/ld`.

Find your linker version:

```
$ /usr/bin/ld -v
@(#)PROGRAM:ld  PROJECT:ld64-409.12
BUILD 17:47:51 Sep 25 2018
configured to support archs: armv6 armv7 armv7s arm64 i386 x86_64 x86_64h armv6m armv7k armv7m armv7em arm64e arm64_32
LTO support using: LLVM version 10.0.0, (clang-1000.11.45.5) (static support for 21, runtime is 21)
TAPI support using: Apple TAPI version 10.0.0 (tapi-1000.11.8.2)
```

Add `-mlinker-version=409` when you link:

```
$ ../../dev-tools/clang+llvm-11.0.0-x86_64-apple-darwin/bin/clang++ --std=c++17 -mlinker-version=409 c17.cpp
```

Works.

Ref: https://stackoverflow.com/questions/60934005/clang-10-fails-to-link-c-application-with-cmake-on-macos-10-12
