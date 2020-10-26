# LBRY Seedit

A simple script to help support the lbry network and your favourite creators on it.

# Why did I create it?

The lbry desktop app is cool but it only runs when your computer is on and running the lbry app so this is not always useful.


I have a NAS with some spare storage and a fibre connection; I wanted to use this to help seed content on the lbry network.

This script is intended to be used with the headless lbrynet client.

# How do I use it?

Download the latest lbrynet client and copy it to /usr/local/bin on your server/NAS
https://github.com/lbryio/lbry-sdk


Give the client execute permissions.

```
chmod +x /usr/local/bin/lbrynet
```

Create a service file for lbrynet

```
cp lbrynet.service /etc/systemd/system/lbrynet.service
systemctl enable lbrynet
systemctl start lbrynet
```

You also may want to change some settings

```
lbrynet settings get
lbrynet settings set wallet_dir /path/to/lbry/lbryum
lbrynet settings set download_dir /path/to/lbry/downloads
lbrynet settings set data_dir /path/to/lbry/data
lbrynet settings set config /path/to/lbry/daemon_settings.yml
lbrynet settings set max_connections_per_download 10
```

Then you will want to add the channels you want to seed to the python script.
Change the page count to change the amount of previous videos you would like to download.

Finally, set up a cron job/scheduled task to run every couple of days to automate the process, only new videos will be downloaded.


If you are not using UPNP then you will want to open up TCP port 3333 and UDP port 4444
