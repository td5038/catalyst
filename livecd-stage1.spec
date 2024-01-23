subarch: amd64
version_stamp: livecd-@TIMESTAMP@
target: livecd-stage1
rel_type: default
profile: default/linux/amd64/17.1/desktop/gnome/systemd/merged-usr
snapshot_treeish: [SNAPSHOT_HASH]
source_subpath: default/stage3-amd64-systemd-mergedusr
portage_confdir: /var/tmp/catalyst/config/stages
repos: /var/db/repos/xenia-overlay

livecd/use:
    -gnome-online-accounts
	wayland
	dist-kernel
	fuse
	flatpak
	gstreamer
	lvm
	networkmanager
	nls
	pipewire
	pipewire-alsa
	policykit
	udev
	usb
	screencast
	video_cards_amdgpu
	video_cards_intel
	video_cards_nouveau
	video_cards_radeon
	video_cards_radeonsi
	video_cards_virgl
	video_cards_vmware
	vaapi
	vpx
	xkb

livecd/packages:
	app-admin/sudo
	app-containers/crun
	app-containers/distrobox
	app-containers/podman
	app-editors/nano
	app-emulation/qemu-guest-agent
	app-emulation/spice-vdagent
	app-eselect/eselect-repository
	app-shells/bash-completion
	dev-util/glib-utils
	dev-util/wayland-scanner
	dev-vcs/git
	gnome-base/gnome-light
	gnome-extra/gnome-shell-extensions
	gnome-extra/gnome-software
	gnome-extra/gnome-tweaks
	sys-apps/xdg-desktop-portal
	gui-libs/xdg-desktop-portal-wlr
	sys-apps/xdg-desktop-portal-gnome
	media-fonts/fonts-meta
	media-libs/gstreamer
	media-libs/mesa
	media-video/wireplumber
	net-fs/samba
	net-print/cups
	sys-apps/flatpak
	sys-apps/iproute2
	sys-apps/lsb-release
	sys-apps/mlocate
	sys-apps/xdg-desktop-portal-gtk
	sys-auth/fprintd
	sys-auth/rtkit
	sys-block/gparted
	sys-block/io-scheduler-udev-rules
	sys-boot/grub
	sys-boot/plymouth
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
	xenia-tools/xenia-meta