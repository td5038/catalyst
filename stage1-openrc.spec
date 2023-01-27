subarch: amd64
target: stage1
version_stamp: openrc-@TIMESTAMP@
rel_type: default
profile: default/linux/amd64/17.1
snapshot: stable
source_subpath: default/stage3-amd64-openrc-latest
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --newuse @world
portage_confdir: /var/tmp/catalyst/config/stages
portage_prefix: releng
