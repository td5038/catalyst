subarch: amd64
target: stage4
version_stamp: gnome-systemd-nvidia
rel_type: default
profile: default/linux/amd64/23.0/desktop/gnome/systemd
snapshot_treeish: [SNAPSHOT_HASH]
source_subpath: default/stage3-amd64-systemd-mergedusr
compression_mode: pixz
portage_confdir: /var/tmp/catalyst/config/stages
portage_prefix: releng
repos: /var/db/repos/xenia-overlay
stage4/use:
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
    video_cards_nvidia
	video_cards_radeon
	video_cards_radeonsi
	video_cards_virgl
	video_cards_vmware
	vaapi
	vpx
	xkb
stage4/packages:
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
stage4/empty: /var/tmp /var/cache /tmp 
stage4/rm:
	/boot/initramfs?*.img
	/boot/vmlinuz?*
	/boot/config?*
	/boot/System.map?*
stage4/root_overlay: 
	[CATALYST_DIR]overlay [CATALYST_DIR]nvidia-overlay
stage4/fsscript:
	[CATALYST_DIR]stage4-systemd-nvidia.sh