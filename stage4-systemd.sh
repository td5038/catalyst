#!/bin/bash
dracut --force --no-hostonly --kver $(ls /lib/modules/)
groupadd wheel
chown root:root /etc/sudoers

systemctl enable bluetooth
systemctl enable NetworkManager
systemctl enable cups
systemctl enable systemd-timesyncd
systemctl enable gdm
systemctl enable lvm2-monitor
systemctl enable qemu-guest-agent
systemctl enable spice-vdagentd
systemctl enable zfs.target
systemctl enable zfs-import-cache
systemctl enable zfs-mount
systemctl enable zfs-import.target 
systemctl enable systemd-firstboot

systemctl --global enable pipewire.socket pipewire-pulse.socket wireplumber.service

rm /boot/*.old

cp /boot/vmlinuz* /boot/vmlinuz
cp /boot/initramfs* /boot/initramfs.img
cp /boot/System* /boot/System.map
cp /boot/config* /boot/config

flatpak remote-add flathub https://flathub.org/repo/flathub.flatpakrepo