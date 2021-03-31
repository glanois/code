# DOWNLOAD

https://www.virtualbox.org

https://www.virtualbox.org/wiki/Downloads

## VirtualBox 6.1.18 platform packages

Click "OS X hosts" (eg, VirtualBox-6.1.18-142142-OSX.dmg)

## VirtualBox 6.1.18 platform packages

Click "All supported platforms" (eg, Oracle_VM_VirtualBox_Extension_Pack-6.1.18.vbox-extpack)

Double-click that file (it installs itself).


# INSTALL

Run VirutalBox

Click "New"

Mount the .iso, using Settings->Storage->Optical Drive.

Click "Start".

In the Ubuntu screen, click "Install".

Unmount the .iso.  (You'll be prompted before the first reboot.)

# CUSTOMIZE

## Guest Additions

You need to install the guest additions before you can do certain things (like use the clipboard to copy/paste between host and guest).

https://superuser.com/questions/1318231/why-doesnt-clipboard-sharing-work-with-ubuntu-18-04-lts-inside-virtualbox-5-1-2

### Method 1 - from Linux command line

```
sudo apt-get update
sudo apt-get install virtualbox-guest-x11
sudo apt-get install virtualbox-guest-dkms
```

(Note - `virtualbox-guest-x11` includes `virtualbox-guest-utils`)

### Method 2 - from VirtualBox menu bar

Devices->Insert Guest Additions CD Image...


## Screen

In Ubuntu, Settings->Display
- Choose "1440x900 (16:10)"

## Super Key

In MacOS, Virtual Box->Preferences->Input->Virtual Machine
- Set "Host Key Combination" to "Right (command)" (is "Left (command)" 
by default).

## Clipboard

In MacOS, Virtual Box->(your VM)->Settings->General->Advanced->Shared Clipboard
- Select "Bidirectional"


## Install

(See Guest Additions above.)

```
sudo apt install gcc
sudo apt install g++
sudo apt install make
sudo apt install git
sudo apt install python3
```

## Shared Folder

### Host Side Configuration

In MacOS, Virtual Box->Settings->Shared Folders - click the 'add folder' icon (upper right).

Select a folder to share (typically put in in the VM folder and call it `share`).

Check the automount check box.

Leave the mount point empty.

### Guest OS Side Configuration

Install the guest addtions as described above.

Add yourself to the `vboxsf` group:
```
sudo adduser <username> vboxsf
```

Reboot.

Test it:
```
touch /media/sf_share/testfile
```

# PERSONALIZE

## bash

Put aliases in ~/.bash_aliases

