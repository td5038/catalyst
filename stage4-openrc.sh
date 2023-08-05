#!/bin/bash
merge-usr
dracut --force --no-hostonly --kver $(ls /lib/modules/)
echo "root:87658765XeniaLinux" | chpasswd
chown root:root /etc/sudoers

cp /etc/passwd /.recovery/etc/passwd
cp /etc/shadow /.recovery/etc/shadow

echo "recovery:x:1000:1000::/home/recovery:/bin/bash" >> /.recovery/etc/passwd
echo "recovery:$6$ovJXS/P4rKaURNaD$IUmaP2JW5uiJgrFVr31bEMb6kEF.ARL.x23m.qvyJ3.oRRbJ1qQ/pU5R2VocEzunYqSGF/YvLFGqF5gn0BQY90:19574::::::" >> /.recovery/etc/shadow

sed s/wheel:x:10:root/wheel:x:10:root,recovery/ /etc/group > /.recovery/etc/group

rm /boot/*.old

cp /boot/vmlinuz* /boot/vmlinuz
cp /boot/initramfs* /boot/initramfs.img
cp /boot/System* /boot/System.map
cp /boot/config* /boot/config

flatpak remote-add flathub https://flathub.org/repo/flathub.flatpakrepo

#eselect repository add xenia-overlay git https://gitlab.com/xenia-group/xenia-overlay.git
#emaint sync --repo xenia-overlay
