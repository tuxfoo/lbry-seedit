#!/bin/python3

# Put the LBRY channel URL here
# You can find it by going to a channel and clicking the "about" tab
channels = [
    "lbry://@TheLinuxGamer#f",
    "lbry://@tuxfoo#e",
    "lbry://@veritasium#f",
    "lbry://@johnstossel#7",
]
# Will only download last x amount of videos according to the following value
max_vids = 5
# Max disk usage allowed in GB
# Older videos will be deleted, set to 0 to disable
max_disk_usage = 0
# At which percent should older videos be deleted
usage_percent = 90
# Videos from these channels will not be deleted when disk is near capacity
never_delete = [
    "@TheLinuxGamer",
    "@tuxfoo"
]
# Only the blobs are required for seeding, clean downloads each time the script is run?
clear_downloads = True
# If you are using docker then leave this as /home/lbrynet/
lbrynet_home = "/home/lbrynet/"

# Versioning, in case we need to back this file up before updating this file in the future.
version = 0
