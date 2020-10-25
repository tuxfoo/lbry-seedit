import json, subprocess

# Basic Script for Seeding LBRY Content

# Put the LBRY channel URL here
# You can find it by going to a channel and clicking the "about" tab
channels = ["lbry://@TheLinuxGamer#f","lbry://@tuxfoo#e","lbry://@veritasium#f","lbry://@johnstossel#7"]
# Will only download last x amount of videos according to the following value
page_size = 5

for channel in channels:
    print("Checking " + channel)
    file = open("channel_data.json", "w")
    subprocess.call("lbrynet claim search --channel=" + channel + " --stream_type=video --page_size=" + str(page_size) + " --order_by=release_time", stdout=file, shell=True)
    with open("channel_data.json", "r") as read_file:
        data = json.load(read_file)
        for item in data['items']:
            print(item['canonical_url'])
            subprocess.call("lbrynet get " + item['canonical_url'], shell=True)
