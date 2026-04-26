# MacOS X Cleanup

When you migrate from MacOS X to Linux, you will bring some unwanted dot files with you.

This is a guide to finding and deleting those files.

## Find Files
```
find . \( -name ".DS_Store" -o -name "._*" -o -name ".localized" \) -type f -print
find . \( -name ".fseventsd" -o -name ".Spotlight-V100" -o -name ".Trashes" -o -name ".TemporaryItems" -o -name "__MACOSX" \) -type d -print
```

## Delete Files

```
find . \( -name ".DS_Store" -o -name "._*" -o -name ".localized" \) -type f -delete -print

# Force-delete the directories (this handles non-empty ones)
find . \( -name ".fseventsd" -o -name ".Spotlight-V100" -o -name ".Trashes" -o -name ".TemporaryItems" -o -name "__MACOSX" \) -type d -exec rm -rf {} + -print
```

