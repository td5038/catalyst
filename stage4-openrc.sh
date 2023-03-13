#!/bin/bash
dracut --force -a "lvm dmsquash-live"
useradd xenia
groupadd sudo
usermod -aG sudo xenia
echo "root:87658765XeniaLinux" | chpasswd
echo "xenia:87658765XeniaLinux" | chpasswd
chown root:root /etc/sudoers