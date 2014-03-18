Usage
=====

    fix-update-tgz.py KoboRoot-orig.tgz KoboRoot-fixed.tgz

What does it do?
================

You can use this script to create a rooted firmware update based on one of the
official firmware update archives. You can find a list of firmware updates
on the [mobileread forum](http://www.mobileread.com/forums/showthread.php?t=185660).

The 'fixed' update can simply be copied to the `.kobo` directory on your Kobo 
eReader and will be installed when you reboot the device. Note that you'll have
to rename the archive to `KoboRoot.tgz` for it to be installed.

The following modifications are made to the firmware:

  * the hostname is set to `kobo`
  * `/etc/services` is restored
  * `/etc/inittab` is updated to start `inetd`
  * `/etc/inetd.conf` is updated to start a `telnet` and `ftp` server
  * if present, `/mnt/onboard/boot.sh` is executed after each boot

**Warning:** by default, the `root` user on the Kobo does not have a password,
which makes this a pretty insecure setup.
