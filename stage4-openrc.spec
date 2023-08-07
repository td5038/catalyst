subarch: amd64
target: stage4
version_stamp: openrc-@TIMESTAMP@
rel_type: default
profile: default/linux/amd64/17.1/desktop/gnome
snapshot: 2023.03.12
source_subpath: default/stage3-amd64-openrc-@TIMESTAMP@
compression_mode: pixz
portage_confdir: /var/tmp/catalyst/config/stages
portage_prefix: releng
portage_overlay: /var/db/repos/xenia-overlay
stage4/use:
	-gnome-online-accounts
	wayland
	dist-kernel
	fuse
	flatpak
	gstreamer
	lvm
	networkmanager
	pipewire
	pipewire-alsa
	policykit
	udev
	usb
	screencast
	video_cards_intel
	video_cards_nouveau
	video_cards_radeon
	video_cards_radeonsi
	video_cards_virgl
	video_cards_vmware
	vaapi
	vpx
	xkb
stage4/packages:
	app-admin/sudo
	app-admin/sysklogd
	app-containers/crun
	app-containers/distrobox
	app-containers/podman
	app-editors/nano
	app-emulation/qemu-guest-agent
	app-emulation/spice-vdagent
	app-eselect/eselect-repository
	app-shells/bash-completion
	dev-util/wayland-scanner
	dev-vcs/git
	gnome-base/gnome-light
	gnome-extra/gnome-browser-connector
	gnome-extra/gnome-shell-extensions
	gnome-extra/gnome-software
	gnome-extra/gnome-tweaks
	gui-libs/display-manager-init
	sys-apps/xdg-desktop-portal
	gui-libs/xdg-desktop-portal-wlr
	sys-apps/xdg-desktop-portal-gnome
	media-fonts/fonts-meta
	media-libs/gstreamer
	media-libs/mesa
	net-fs/samba
	net-misc/chrony
	net-print/cups
	sys-apps/flatpak
	sys-apps/iproute2
	sys-apps/lsb-release
	sys-apps/merge-usr
	sys-apps/mlocate
	sys-apps/xdg-desktop-portal-gtk
	sys-auth/fprintd
	sys-auth/rtkit
	sys-block/gparted
	sys-boot/grub
	sys-fs/bcache-tools
	sys-fs/btrfs-progs
	sys-fs/cryptsetup
	sys-fs/dmraid
	sys-fs/dosfstools
	sys-fs/e2fsprogs
	sys-fs/exfatprogs
	sys-fs/f2fs-tools
	sys-fs/fuse-exfat
	sys-fs/fuse-overlayfs
	sys-fs/fuseiso
	sys-fs/go-mtpfs
	sys-fs/jfsutils
	sys-fs/lsscsi
	sys-fs/lvm2
	sys-fs/mac-fdisk
	sys-fs/mdadm
	sys-fs/multipath-tools
	sys-fs/ntfs3g
	sys-fs/squashfs-tools
	sys-fs/xfsprogs
	sys-fs/zfs
	sys-fs/zfs-kmod
	sys-kernel/gentoo-kernel-bin
	sys-kernel/linux-firmware
	sys-power/power-profiles-daemon
	sys-process/cronie
	xenia-tools/foxsnapshot
stage4/rcadd:
	bluetooth|default
	cupsd|default
	cronie|default
	chronyd|default
	display-manager|default
	elogind|boot
	lvm|boot
	qemu-guest-agent|default
	sshd|default
	sysklogd|default
	spice-vdagent|default
	udev|sysinit
	zfs-import|boot
	zfs-mount|boot
stage4/empty: /var/tmp /var/cache /tmp 
stage4/rm: 
	/usr/share/gdm/autostart/LoginWindow/spice-vdagent.desktop
	/usr/share/gdm/greeter/autostart/spice-vdagent.desktop
	/usr/share/gnome-background-properties/adwaita.xml
	/boot/initramfs?*.img
	/boot/vmlinuz?*
	/boot/config?*
	/boot/System.map?*
stage4/root_overlay: [CATALYST_DIR]overlay
stage4/fsscript: [CATALYST_DIR]stage4-openrc.sh
