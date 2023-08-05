# !/bin/bash

echo "--- foxmount ---"

echo "foxmount: Mounting roots"
mount -L ROOTS /sysroot/roots

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

recovery() {
    echo "foxmount: Unmounting overlays"
    umount -l /sysroot/usr
    umount -l /sysroot/etc
    umount -l /sysroot/var
    echo "foxmount: Mounting recovery"
    cd /sysroot/.recovery && for d in */ ; do      
        mount -t overlay overlay -o lowerdir=/sysroot/$d:/sysroot/.recovery/$d /sysroot/$d
    done

}

echo "foxmount: Checking for recovery"
for p in $(getargs recovery=); do
    if [ $p = "true" ]; then
        recovery
        exit
    fi
done

echo "foxmount: Checking for config"
if [ -f "/sysroot/roots/foxmount.sh" ]; then
    echo "foxmount: Running config"
    source /sysroot/roots/foxmount.sh
    exit
fi


if [[ $(get_filesystem OVERLAY) != "" ]]
then
    echo "foxmount: Overlays on label, traditional FS layout"

    cd /sysroot/.recovery && for d in */ ; do
        mkdir -p /sysroot/roots/.recovery/.$d
        mkdir -p /sysroot/roots/.recovery/.w_$d
        mount -t overlay overlay -o lowerdir=/sysroot/.recovery/$d:/sysroot/$d,upperdir=/sysroot/roots/.recovery/.$d,workdir=/sysroot/roots/.recovery/.w_$d /sysroot/$d
    done
}

foxmount() {
    echo "foxmount: Checking for recovery"
    for p in $(getargs recovery=); do
        if [ $p = "true" ]; then
            recovery
            return 0
        fi
    done

    echo "foxmount: Checking for config"
    if [ -f "/sysroot/roots/foxmount.sh" ]; then
        echo "foxmount: Running config"
        source /sysroot/roots/foxmount.sh
        return 0
    fi


    if [[ $(get_filesystem OVERLAY) != "" ]]
    then
        echo "foxmount: Overlays on label, traditional FS layout"

        echo "foxmount: Mounting overlay location"
        mount -L OVERLAY /sysroot/overlay
        
        echo "foxmount: Mounting home"
        mount -L HOME /sysroot/home

    # cow: please help mount ZFS?
else
    echo "foxmount: FATAL: could not find overlays!"
    recovery
    exit
fi

        echo "foxmount: Mounting overlay subvolume"
        mount -L ROOTS -o subvol=overlay /sysroot/overlay

        echo "foxmount: Mounting home"
        mount -L ROOTS -o subvol=home /sysroot/home

echo "foxmount: Checking for foxsnapshot revert"
if [ -s /sysroot/roots/.revert ]; then
    btrfs subvolume delete /sysroot/overlay/usr
    btrfs subvolume snapshot /sysroot/roots/.foxsnapshot/$(cat /sysroot/roots/.revert) /sysroot/overlay/usr
fi

echo "foxmount: Mounting overlays on /sysroot"
mount -t overlay overlay -o lowerdir=/sysroot/usr,upperdir=${usr_path}/usr,workdir=${usr_path}/usrw,ro /sysroot/usr
mount -t overlay overlay -o lowerdir=/sysroot/etc,upperdir=${etc_path}/etc,workdir=${etc_path}/etcw,rw /sysroot/etc
mount -t overlay overlay -o lowerdir=/sysroot/var,upperdir=${var_path}/var,workdir=${var_path}/varw,rw /sysroot/var
echo "foxmount: Finished mounting overlays"
