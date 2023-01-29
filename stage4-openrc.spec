subarch: amd64
target: stage4
version_stamp: openrc-@TIMESTAMP@
rel_type: default
profile: default/linux/amd64/17.1
snapshot: stable
source_subpath: default/stage3-amd64-openrc-@TIMESTAMP@
compression_mode: pixz
portage_confdir: /var/tmp/catalyst/config/stages
portage_prefix: releng
stage4/use:
	lvm
	udev
stage4/packages:
	net-misc/dhcpcd
	app-misc/neofetch
	sys-boot/grub
	sys-fs/lvm2
	sys-kernel/linux-firmware
    sys-fs/e2fsprogs
    sys-fs/dosfstools
    sys-apps/iproute2
    app-editors/nano
	sys-apps/lsb-release
	sys-kernel/gentoo-kernel-bin
	sys-fs/squashfs-tools
	app-admin/sudo
	sys-apps/flatpak
stage4/rcadd:
	lvm|boot
	sshd|default
	udev|sysinit
stage4/empty: /var/tmp /var/cache /var/lock /var/log /var/run /var/spool /tmp
stage4/root_overlay: [CATALYST_DIR]overlay
stage4/fsscript: [CATALYST_DIR]stage4-openrc.sh
