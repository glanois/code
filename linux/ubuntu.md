# Introduction

These notes generally apply to Ubuntu 18.04 (and possibly later).

# Enable Remote Desktop Sharing

First, enable screen sharing:

  - Settings > Sharing > Screen Sharing
    - Set to ON
    - Username authentication does not work, therefore you must set
    'Access Options' to 'Require a password' (and set a password)


Neither Mac OS X Screen Sharing nor VNC Viewer understand Vino's encryption.  
Therefore you must disable encryption:

```
$ gsettings set org.gnome.Vino require-encryption false

$ gsettings list-recursivle org.gnome.Vino | grep encrypt
```
