#!/bin/bash
merge-usr
dracut --force -a "lvm dmsquash-live"
useradd xenia
groupadd wheel
usermod -aG wheel xenia
echo "root:87658765XeniaLinux" | chpasswd
echo "xenia:87658765XeniaLinux" | chpasswd
chown root:root /etc/sudoers

rm /boot/*.old

cp /boot/vmlinuz* /boot/vmlinuz
cp /boot/initramfs* /boot/initramfs.img
cp /boot/System* /boot/System.map
cp /boot/config* /boot/config

flatpak remote-add flathub https://flathub.org/repo/flathub.flatpakrepo