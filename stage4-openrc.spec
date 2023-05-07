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
stage4/use:
	-qt5
	-kde
	video_cards_intel
	video_cards_nouveau
	video_cards_radeon
	video_cards_radeonsi
	video_cards_virgl
	video_cards_vmware
	lvm
	udev
	pipewire
	pipewire-alsa
	fuse
	networkmanager
	usb
	python_targets_python3_10
	-gnome-online-accounts
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
	dev-vcs/git
	app-arch/pixz
	dev-util/catalyst
	media-libs/mesa
	dev-util/wayland-scanner
	sys-apps/xdg-desktop-portal-gtk
	gui-libs/xdg-desktop-portal-wlr
	gnome-base/gnome-light
	gnome-extra/gnome-software
	gnome-extra/gnome-shell-extensions
	gnome-extra/gnome-browser-connector
	gnome-extra/gnome-tweaks
	gui-libs/display-manager-init
	media-fonts/fonts-meta
	app-containers/crun
	app-containers/podman
	app-containers/distrobox
	net-print/cups
	net-fs/samba
stage4/rcadd:
	lvm|boot
	elogind|boot
	display-manager|default
	sshd|default
	udev|sysinit
	cupsd|default
stage4/empty: /var/tmp /var/cache /var/lock /var/log /var/run /var/spool /tmp
stage4/root_overlay: /home/luna/.foxpkg/catalyst/overlay
stage4/fsscript: /home/luna/.foxpkg/catalyst/stage4-openrc.sh
