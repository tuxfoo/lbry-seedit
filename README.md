# LBRY Seedit

A simple script to help support the lbry network and your favourite creators on it.

# Why did I create it?

The lbry desktop app is cool but it only runs when your computer is on and running the lbry app.


I have a NAS with some spare storage and a fibre connection; I wanted to use this to help seed content on the lbry network.

This script is intended to be used with the headless lbrynet client.

# How do I use it?

Download the latest lbrynet client and copy it to /usr/local/bin on your server/NAS


Give the client execute permissions.

```
chmod +x /usr/local/bin/lbrynet
```

You might want to use screen to  start the daemon

```
screen lbrynet start
```
ctrl+d to detach


You also may want to change some settings

```
lbry settings get
lbry settings set wallet_dir /path/to/lbry/lbryum
lbry settings set download_dir /path/to/lbry/downloads
lbry settings set data_dir /path/to/lbry/data
lbry settings set config /path/to/lbry/daemon_settings.yml
```

Then you will want to add the channels you want to seed to the python script.
Change the page count to change the amount of previous videos you would like to download.

Finally, set up a cron job/scheduled task to run every couple of days to automate the process, only new videos will be downloaded.
