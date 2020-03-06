# Create a Bootable USB Stick on MacOS

https://tutorials.ubuntu.com/tutorial/tutorial-create-a-usb-stick-on-macos#0

Summary: use a 2GB or greater USB stick, run Disk Utility and
erase, format as MS-DOS FAT, and then run Etcher to write .iso to it.


# Boot From USB Stick

Power down Mac.  Insert USB stick.  Power on and hold down Option key.
When you get get to boot screen, choose EFI.  (If there are two, choose
the one on the right.)


You will see a black and white screen with options to Try Ubuntu and 
Install Ubuntu. With "Try Ubuntu" selected, press "e" to edit the boot entry.

Edit the line that begins with linux and place the word "nomodeset" after 
"quiet splash".  (You can also get rid of "quiet splash".  But you need
the "nomodeset" to be in there.)

Press F10.

Ubuntu boots into trial mode.

Double-click the icon marked "Install Ubuntu".

(From https://www.macworld.co.uk/how-to/mac/how-install-linux-on-mac-3637265/)


# Make nomodeset a Permanent Option in Grub.

If/when you reboot after the install, you will still have problems.

The solution is to add "nomodeset" to the Grub config file.

You need to reboot in trial mode again (adding "nomodeset" to the boot
parameters as you did the first time).

Once you are up and running in trial mode, open a Terminal window.

1. Run gparted from the command line (with '&' to run in the
background).  Find the hard drive partition where Ubuntu was
installed.  It will be of type ext4.  For example, /dev/sda2.

1. Mount this partition: 
    `$ sudo mount /dev/sdXY /mnt`

1. Then mount/bind the directories Grub needs to access (all on one line):  
    ```
    $ sudo mount --bind /dev /mnt/dev &&
    sudo mount --bind /dev/pts /mnt/dev/pts &&
    sudo mount --bind /proc /mnt/proc &&
    sudo mount --bind /sys /mnt/sys
    ```

1. Then move on to this environment using chroot:
    `$ sudo chroot /mnt`

1. Edit /etc/default/grub
    `$ sudo nano /etc/default/grub`
    Change the line to be `GRUB_CMDLINE_LINUX_DEFAULT="nomodeset"`
    Remove `quiet splash` so you can watch some of the bootup logging.

1. Push the update out to the actual config file:
    `$ sudo update-grub`
    https://askubuntu.com/questions/38780/how-do-i-set-nomodeset-after-ive-already-installed-ubuntu#38782

1. Install Things
    Do an update first:
    ```
    $ sudo apt update

    # SSH
    $ sudo apt install openssh-server
    $ sudo systemctl status ssh

    # GCC (gcc and g++):
    $ sudo apt install build-essential
    $ sudo apt update

    # SSH
    $ sudo apt install openssh-server
    $ sudo systemctl status ssh

    # GCC (gcc and g++):
    $ sudo apt install build-essential
    $ sudo apt install socat
    $ sudo apt install python2.7
    $ sudo apt install emacs
    $ sudo apt install git
    $ sudo apt install cmake
    ```

# First Attempt Notes

3. At the Grub menu, highlight Install.  Press the 'e' key.  At the end of
the line containing "quiet splash", add "acpi=off" between "quiet splash" and 
"---".  Press F10 to boot.

Remove "quiet" and "splash" to diagnose boot problems.

/dev/sr0 no medium found

More info:

https://bugs.launchpad.net/ubuntu/+bug/500822
https://bugs.launchpad.net/ubuntu/+source/usb-creator/+bug/492301/comments/17
https://askubuntu.com/questions/47076/usb-boot-problems


May have to punt and just burn a DVD and boot off that.

DVD did not work - suspect internal DVD drive is bad.

External DVD did not work.

Went back to USB stick, and started using "nomodeset".
