# !/bin/bash

etc_path="/sysroot/overlay"
var_path="/sysroot/overlay"
usr_path="/sysroot/overlay"

get_filesystem() {
    label="$1"

    # Get the partition information using the 'blkid' command
    partition_info=$(blkid -o value -s TYPE -l -t LABEL="$label")

    # Extract the filesystem from the partition information
    filesystem=$(echo "$partition_info" | awk 'NR==1{print}')

    # Return the filesystem
    echo "$filesystem"
}

echo "--- foxmount ---"

echo "foxmount: Mounting roots"
mount -L ROOTS /sysroot/roots

if [[ $(get_filesystem OVERLAY) != "" ]]
then
    echo "foxmount: Overlays on label, traditional FS layout"

    echo "foxmount: Mounting overlay location"
    mount -L OVERLAY /sysroot/overlay
    
    echo "foxmount: Mounting home"
    mount -L HOME /sysroot/home

elif [[ $(get_filesystem ROOTS) = "btrfs" ]]
then
    echo "foxmount: btrfs found"

    echo "foxmount: Mounting overlay subvolume"
    mount -L ROOTS -o subvol=overlay /sysroot/overlay

    echo "foxmount: Mounting home"
    mount -L ROOTS -o subvol=home /sysroot/home

    echo "foxmount: Setting overlay paths"
    etc_path="/sysroot/overlay/etc"
    var_path="/sysroot/overlay/var"
    usr_path="/sysroot/overlay/usr"

elif [[ $(get_filesystem XENIA) = "zfs_member" ]] # this won't work, no label on ZFS - find another way
then
    echo "foxmount: zfs found"
    /sbin/modprobe zfs

    # cow: please help mount ZFS?
else
    echo "foxmount: FATAL: could not find overlays!"
    exit
fi

echo "foxmount: Creating overlay directories if they don't exist"
[ ! -d "${etc_path}/etc" ] && mkdir ${etc_path}/etc
[ ! -d "${var_path}/var" ] && mkdir ${var_path}/var
[ ! -d "${usr_path}/usr" ] && mkdir ${usr_path}/usr

echo "foxmount: Creating overlay work directories if they don't exist"
[ ! -d "${etc_path}/etcw" ] && mkdir ${etc_path}/etcw
[ ! -d "${var_path}/varw" ] && mkdir ${var_path}/varw
[ ! -d "${usr_path}/usrw" ] && mkdir ${usr_path}/usrw

echo "foxmount: Mounting overlays on /sysroot"
mount -t overlay overlay -o lowerdir=/sysroot/etc,upperdir=${etc_path}/etc,workdir=${etc_path}/etcw,rw /sysroot/etc
mount -t overlay overlay -o lowerdir=/sysroot/var,upperdir=${var_path}/var,workdir=${var_path}/varw,rw /sysroot/var
mount -t overlay overlay -o lowerdir=/sysroot/usr,upperdir=${usr_path}/usr,workdir=${usr_path}/usrw,ro /sysroot/usr
echo "foxmount: Finished mounting overlays"