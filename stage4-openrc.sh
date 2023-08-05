#!/bin/bash
merge-usr
dracut --force --no-hostonly --kver $(ls /lib/modules/)
useradd recovery
useradd xenia
usermod -aG wheel xenia
echo "xenia:87658765XeniaLinux" | chpasswd
chown root:root /etc/sudoers

rm /boot/*.old

cp /boot/vmlinuz* /boot/vmlinuz
cp /boot/initramfs* /boot/initramfs.img
cp /boot/System* /boot/System.map
cp /boot/config* /boot/config

flatpak remote-add flathub https://flathub.org/repo/flathub.flatpakrepo

#eselect repository add xenia-overlay git https://gitlab.com/xenia-group/xenia-overlay.git
#emaint sync --repo xenia-overlay
