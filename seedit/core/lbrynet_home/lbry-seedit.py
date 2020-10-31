#!/bin/python3
import json, subprocess, sys, time, os, psutil

# Basic Script for Seeding LBRY Content

# Put the LBRY channel URL here
# You can find it by going to a channel and clicking the "about" tab
channels = [
    "lbry://@TheLinuxGamer#f",
    "lbry://@tuxfoo#e",
    "lbry://@veritasium#f",
    "lbry://@johnstossel#7",
]
# Will only download last x amount of videos according to the following value
page_size = 5

# processes = filter(lambda p: psutil.Process(p).name() == "lbrynet", psutil.pids())

# scripts = []
# paths = []

# for pid in processes:
#     try:
#         scripts.append(psutil.Process(pid).cmdline()[0])
#     except IndexError:
#         pass

# for script in scripts:
#     paths.append(os.path.abspath(script))

# try:
#     lbrynet = paths[0]
# except IndexError:
#     if os.path.isfile(sys.path[0] + "/lbrynet"):
#         subprocess.Popen(sys.path[0] + "/lbrynet start", close_fds=True, shell=True)
#         lbrynet = sys.path[0] + "/lbrynet"
#         time.sleep(15)
#     else:
#         raise Exception("LBRY is not running, start LBRY or place lbrynet in my directory!")

for channel in channels:
    print("Checking " + channel)
    command = [
        "lbrynet",
        "claim",
        "search",
        f"--channel={channel}",
        "--stream_type=video",
        f"--page_size={page_size}",
        "--order_by=release_time",
    ]
    print(f"command: {' '.join(command)}")
    process_output = subprocess.run(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True
    )
    deamon_not_running_msg = "Could not connect to daemon. Are you sure it's running?"

    if process_output.returncode == 1:
        print(f"Error: {process_output.stderr.decode()}")
        sys.exit(1)
    if deamon_not_running_msg in process_output.stdout.decode():
        print(deamon_not_running_msg)
        sys.exit(1)

    data = json.loads(process_output.stdout.decode())
    for item in data["items"]:
        print(item["canonical_url"])
        subprocess.call("lbrynet get " + item["canonical_url"], shell=True)
