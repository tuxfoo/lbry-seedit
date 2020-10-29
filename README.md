# LBRY Seedit

A simple script to help support the lbry network and your favourite creators on it.

# Why did I create it?

The lbry desktop app is cool but it only runs when your computer is on and running the lbry app so this is not always useful.


I have a NAS with some spare storage and a fibre connection; I wanted to use this to help seed content on the lbry network.

This script is intended to be used with the headless lbrynet client.

# How do I use it?
Make sure you have Docker and Docker-compose installed. You can find directions on how to install them here:
- [Install Docker](https://docs.docker.com/install/)
- [Install docker-compose](https://docs.docker.com/compose/install/)

You will first need to build the docker image by running `docker-compose build` from the repo base directory.

Once that finishes, run `docker-compose up -d` to start the container (the `-d` just runs it in the background).

Then you will want to add the channels you want to seed to the python script.
Change the page count to change the amount of previous videos you would like to download.

Now to start the python script run `make run-seedit` which will run the makefile target that runs the python script in the docker container.

Finally, set up a cron job/scheduled task to run every couple of days to automate the process, only new videos will be downloaded.
