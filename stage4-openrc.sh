#!/bin/bash
dracut --force -a "lvm dmsquash-live"
useradd xenia
groupadd wheel
usermod -aG wheel xenia
echo "root:87658765XeniaLinux" | chpasswd
echo "xenia:87658765XeniaLinux" | chpasswd
chown root:root /etc/sudoers