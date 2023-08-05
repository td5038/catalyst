#!/bin/bash
dracut --force --no-hostonly --kver $(ls /lib/modules/)
useradd recovery
usermod -aG wheel recovery
chown root:root /etc/sudoers

cp /etc/passwd /.recovery/etc/passwd
cp /etc/shadow /.recovery/etc/shadow

echo "recovery:$6$ovJXS/P4rKaURNaD$IUmaP2JW5uiJgrFVr31bEMb6kEF.ARL.x23m.qvyJ3.oRRbJ1qQ/pU5R2VocEzunYqSGF/YvLFGqF5gn0BQY90:19574::::::" >> /.recovery/etc/shadow

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

#eselect repository add xenia-overlay git https://gitlab.com/xenia-group/xenia-overlay.git
#emaint sync --repo xenia-overlay
