#!/bin/python3
import json, subprocess, sys, time, os, psutil

# Basic Script for Seeding LBRY Content

# Put the LBRY channel URL here
# You can find it by going to a channel and clicking the "about" tab
channels = ["lbry://@TheLinuxGamer#f","lbry://@tuxfoo#e","lbry://@veritasium#f","lbry://@johnstossel#7"] 
# Will only download last x amount of videos according to the following value
page_size = 5

processes = filter(lambda p: psutil.Process(p).name() == "lbrynet", psutil.pids())

scripts = []
paths = []

for pid in processes:
    try:
        scripts.append(psutil.Process(pid).cmdline()[0])
    except IndexError:
        pass

for script in scripts:
    paths.append(os.path.abspath(script))

try:
    lbrynet = paths[0]
except IndexError:
    if os.path.isfile(sys.path[0] + "/lbrynet"):
        subprocess.Popen(sys.path[0] + "/lbrynet start", close_fds=True, shell=True)
        lbrynet = sys.path[0] + "/lbrynet"
        time.sleep(15)
    else:
        raise Exception("LBRY is not running, start LBRY or place lbrynet in my directory!")

for channel in channels:
    print("Checking " + channel)
    file = open("channel_data.json", "w")
    subprocess.call(lbrynet + " claim search --channel=" + channel + " --stream_type=video --page_size=" + str(page_size) + " --order_by=release_time", stdout=file, shell=True)
    with open("channel_data.json", "r") as read_file:
        data = json.load(read_file)
        for item in data['items']:
            print(item['canonical_url'])
            subprocess.call(lbrynet + " get " + item['canonical_url'], shell=True)
