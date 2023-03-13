# Catalyst rootFS generation

To build the Xenia rootFS, we use the gentoo tool Catalyst.

All the spec files are here, as well as the `/var/tmp/catalyst/config` directory (in development we symlink to the config folder in this directory). There is a `build.sh` file included for reference (it is NOT intended to be executed, but will work).

The default root password is `87658765XeniaLinux`. This can be changed in `stage4-openrc.sh`.

An account called xenia is also created with the same password. This account has sudo privileges.

## Notes

The stage4 is built with `/etc/catalyst/catalystrc` containing the following extra environment variables:

```
GRUB_PLATFORMS="efi-64"
VIDEO_CARDS="*"
```