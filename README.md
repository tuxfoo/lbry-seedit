# LBRY Seedit

A simple script to help support the lbry network and your favourite creators on it.

# Why did I create it?

The lbry desktop app is cool but it only runs when your computer is on and running the lbry app so this is not always useful.

I have a NAS with some spare storage and a fibre connection; I wanted to use this to help seed content on the lbry network.

This script is intended to be used with the headless lbrynet client.

# How do I use it?

# Docker

You will first need to install docker.

Download the prebuilt container.

```
docker pull tuxfoo/lbry-seedit:latest
```

Run the container replacing the destination path with to location of where you would like to store hosted data.

```
docker run -v /path/to/lbrydata_dest:/home/lbrynet -d --name seedit tuxfoo/lbry-seedit:latest
```

`seedit_config.yaml` will be shown in `/path/to/lbrydata_dest` after docker started successfully.

Edit the `seedit_config.yaml` file which will be stored in the destination volume from the previous command.

Add/change channel to host, and set the storage limit in `seedit_config.yaml`.



# Open ports

If you are not using UPNP then you will need to open up TCP port 3333 and UDP port 4444 on your router/firewall.



# Building it yourself

Make sure you have make, Docker and Docker-compose installed. You can find directions on how to install them here:
- [Install Docker](https://docs.docker.com/install/)
- [Install docker-compose](https://docs.docker.com/compose/install/)

Clone this repo to the partition where you plan to store all the hosting data.

You will first need to build the docker image by running `docker-compose build` from the repo base directory.

Once that finishes, run `docker-compose up -d` to start the container (the `-d` just runs it in the background).

Then you will want to add the channels you want to seed to seedit_config.yaml.
Change the page count to change the amount of previous videos you would like to download.

Now to start the python script run `make run-seedit` which will run the makefile target that runs the python script in the docker container.

Cron job is running inside docker container inside seedit/core/lbrycron file you can adjust it if you do not want script to run every 12h.
Editing cron will require you to rebuild container with `docker-compose build` then `docker-compose up -d`.

If you are not using UPNP then you will need to open up TCP port 3333 and UDP port 4444

# Non-Docker Version

Going forward, lbry-seedit will be developed with docker in mind.
If you do not want the docker version, then you can just download the python script from seedit/core/lbrynet_home and set up a cron job for it, make sure the lbrynet client is also installed and running.

# Disk storage management
The python script also contains support for basic disk storage management. Change the value of "max_disk_usage" to enable this feature; it will delete the oldest videos first excluding videos from channels listed in "never_delete".
