#! /usr/bin/env python3

import sys
import os

import requests

from settings import API_KEY

def print_usage():
    file_name = os.path.basename(__file__)
    print(f"Usage: ./{file_name} TORRENTNAME")
    print(f"{file_name} is a short script to send push notifications when rtorrent downloads have completed")    

def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)
    
    torrent_name = sys.argv[1]
    notification_title = "Seedbox download finished"
    notification_text = f"{torrent_name} has finished downloading"
    url = f"https://joinjoaomgcd.appspot.com/_ah/api/messaging/v1/sendPush?apikey={API_KEY}&deviceId=group.all&title={notification_title}&text={notification_text}"

    requests.get(url)


if __name__ == '__main__':
    main()