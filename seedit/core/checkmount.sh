#!/bin/bash

## TODO: Make a bit more aware of the run mode of this appliance in case there is ever a test mode enabled in the start.sh
mountpoint=/home/lbrynet
declare -p | grep -Ev 'BASHOPTS|BASH_VERSINFO|EUID|PPID|SHELLOPTS|UID' > /container.env
# Copy the python scripts, as this cannot not be done via docker.
if [ ! -f "/home/lbrynet/lbry-seedit.py" ]; then
  cp /seedit/lbry-seedit.py /home/lbrynet/lbry-seedit.py
fi
if [ ! -f "/home/lbrynet/seedit_config.py" ]; then
  cp /seedit/seedit_config.py /home/lbrynet/seedit_config.py
fi
if ! grep -qs ".* $mountpoint " /proc/mounts; then
    echo "$mountpoint not mounted, refusing to run."
    ## TODO: We should have documentation that this error references directly with a URL as to why it won't run without a volume.
    exit 1
else
    crontab /etc/cron.d/lbrycron
    cron
    bash -c "$*"
fi
