all: c17

clean:
	rm c17 *.o

# If you are running Clang via Homebrew, put 
# /usr/local/opt/llvm/bin in your PATH in your .bash_profile

# If you are running Clang from a pre-built binary distribution 
# you downloaded from llvm.org, put 
# /Users/gerard/users/gerard/dev-tools/clang+llvm-11.0.0-x86_64-apple-darwin/bin in your PATH in your .bash_profile

CC = clang
CXX = $(CC)++
CPPSTD = c++17
CPPFLAGS = -std=$(CPPSTD)

AR = llvm-ar

# Set up LDFLAGS.
#
# --verbose displays the internal ld command and all its arguments.
# 
# -mlinker-version=409 resolves the following error:
# ld: unknown option: -platform_version
# 
# See: https://stackoverflow.com/questions/60934005/clang-10-fails-to-link-c-application-with-cmake-on-macos-10-12
LDFLAGS = --verbose -mlinker-version=409

c17.o: c17.cpp
	$(CXX) $(CPPFLAGS) -c c17.cpp

c17: c17.o
	$(CXX) $(LDFLAGS) -o c17 c17.o

