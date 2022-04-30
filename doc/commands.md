# Emacs

| Keystrokes | Command    |
|---------|---------------|
| C-x TAB | indent-rigidly
| M-^     | delete-indentation
|         | count-matches
| M-g g   | goto-line
| C-x r r | copy-rectangle-to-register

# Ack

| Command | Description |
|---------|-------------|
| ack --help-types | Examples: --make --cpp --python --cmake
| ack -g _pattern_ | Find files whose names match _pattern_
| ack -g _pattern1_ \| ack -x _pattern2_ | Find in files whose names are given in stdin
| ack "\[^\\x00-\\x7F]" | Find non-ASCII characters
| ack -g --ignore-ack-defaults --type-set backup:ext:bak --type=backup . | Find .bak files
| ack -g --ignore-ack-defaults --type-set emacs:match:/~$/ --type=emacs . | Find Emacs backup files
| ack -g _stuff_ \| xargs rm | Delete stuff ack found
| ack -l _string1_ \| xargs perl -pi -E 's/_string1_/_string2_/g' | Global search and replace _string1_ with _string2_ (Linux) 
| ack -l _string1_ \| xargs perl -p -i.bak -E "s/_string1_/_string2_/" | Global search and replace _string1_ with _string2_ (Windows)

# Perl

| Command | Description|
|---------|------------|
| perl -wnl -e "/_regex_/ and print;" _filename_ | Use \\x22 to represent double quotes in _regex_
| _something_ \| perl -wnl -e "/_regex_/ and print;" | Search for _regex_in stdin

# Windows

Quick and dirty file find: 
  * DIR /S /B *.h *.cpp

Add shortcuts to Windows Explorer RMB->Send To context menu:
  * C:\\Users\_username_\\AppData\\Roaming\\Microsoft\\Windows\\SendTo

# Linux

| Command | Description
|---------|-------------|
| diff -rq _dir1_ _dir2_ | Recursively compare two directories
| tar cvf - ./_dir_ \| gzip > _dir_.tar.gz | tar and gzip directory
| gunzip --stdout _filename_.tar.gz \| tar tvf - | 't' - table of contents
| gunzip --stdout _filename_.tar.gz \| tar xvf - | 'x' - extract contents
| find . ! -newermt "_YYYY_-_MM_-_DD_ _HH_:_MM_:_SS_"| Find files whose modification time is newer than _YYYY_-_MM_-_DD_ _HH_:_MM_:_SS_"
| dd if=/dev/random count=1 bs=16 status=none \| hexdump -ve '/1 "%04x"'| Generate 1 block of 16 random bytes and print as hex ASCII
| cat _filename_.csv \| (read -r; printf "%s\n" "$REPLY"; sort -t"," -k2) > _filename_-sorted.csv | Sort a CSV file by its 2nd column, keeping the header record as the first record.
| xdg-open _filename_or_url_ | Opens the file or URL in the preferred application.
| lowriter --headless --convert-to odt *.docx | Convert all Microsoft Word files to LibreOffice format.
| ifconfig | grep "inet " | grep -Fv 127.0.0.1 | awk '{print $2}' | Print IP address.
