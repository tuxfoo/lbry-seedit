#!/bin/python3
import json, subprocess, sys, time, os, shutil

import seedit_config as cfg

# Basic Script for Seeding LBRY Content
channels = cfg.channels
page_size = cfg.page_size
max_disk_usage = cfg.max_disk_usage
usage_percent = cfg.usage_percent
never_delete = cfg.never_delete
clear_downloads = cfg.clear_downloads
lbrynet_home = cfg.lbrynet_home


def get_usage():
    size = subprocess.check_output(['du','-s', lbrynet_home]).split()[0].decode('utf-8')
    size = int(size)/1024/1024
    return size

def sort_files():
    command = [
    "lbrynet",
    "file",
    "list",
    "--page_size=1000",
    ]
    process_output = subprocess.run(
    command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True
    )
    videos = json.loads(process_output.stdout.decode())
    sorted_videos = sorted(videos['items'], key=lambda k: int(k['metadata']['release_time']))
    return sorted_videos

def clean_downloads():
    path = lbrynet_home + "Downloads"
    if os.path.exists(path):
        shutil.rmtree(path, ignore_errors=True)

if max_disk_usage > 0:
    if os.path.exists(lbrynet_home):
        if clear_downloads:
            clean_downloads()
        size = get_usage()
        # Once the allowed percentage of the allowed capacity has been reached, free some space.
        if size / max_disk_usage * 100 >= usage_percent:
            sorted_videos = sort_files()
            print("Near max allowed capacity; Will attempt to free space.")
            for video in sorted_videos:
                # Get channel name
                if video['channel_name'] == None:
                    command = [
                    "lbrynet",
                    "claim",
                    "search",
                    f"--claim_ids={video['claim_id']}"
                    ]
                    process_output = subprocess.run(
                    command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True
                    )
                    channel_name = json.loads(process_output.stdout.decode())
                    video['channel_name'] = channel_name['items'][0]['signing_channel']['name']
                if video['channel_name'] not in never_delete:
                    print("Deleting video from: " + video['channel_name'])
                    #lbry command to delete file
                    subprocess.call("lbrynet file delete --delete_from_download_dir --claim_id=" + video['claim_id'], shell=True)
                    #If enough space has been cleared then stop deleting videos.
                    if get_usage() / max_disk_usage * 100 <= usage_percent:
                        break
                    else:
                        print("Still need to clear more space; Deleting another Video...")
                else:
                    print("Skipping Video from: " + video['channel_name'])
        if size / max_disk_usage * 100 >= usage_percent:
            print("Failed to clear enough storage, Quiting")
            quit()

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
    if clear_downloads:
        clean_downloads()
