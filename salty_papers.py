import requests
import time
import urllib.request
import ctypes
import os
import sys
import random
from PIL import Image, ImageOps
CLIENT_ID = 'AERmPCqvfBEALQ'
CLIENT_SECRET = 'mMm2fM63jX1onIXN-0bkdwUDXzk'

wallpaper_fp = "./reddit_wallpaper.png"

def auth_and_update(sub_reddit, post_num=1, resolution=(1920,1080)):

    client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    
    post_data = {"grant_type": "client_credentials", "grant_type":"client_credentials"}
    headers = {"User-Agent": "SaltyPapers/0.1 by ThePythoneer"}
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
    response_header = response.json()
    
    headers = {"Authorization": f"bearer {response_header['access_token']}", "User-Agent": "SaltyPapers/0.1 by ThePythoneer"}
    reddit_url = f"https://oauth.reddit.com/r/{sub_reddit}/.json?limit={post_num}"
    response = requests.get(reddit_url, headers=headers)
    
    print(response.json())
    response = response.json()['data']['children'][-1]['data']

    # img_url = response["preview"]["images"][0]["source"]["url"].replace("&amp;","&")
    img_url = response["url"]
    img_title = response['title']
    
    print(f'Current Wallpaper: {img_title}\n')    
    print(f"Image URL: {img_url}")
    
    #saves image at link to file
    urllib.request.urlretrieve(img_url, wallpaper_fp)
    path = os.path.abspath(wallpaper_fp)
    print(path)
    image = Image.open(path)

    thumb = ImageOps.fit(image, resolution, Image.ANTIALIAS)
    thumb.save(wallpaper_fp)

    SPI_SETDESKWALLPAPER = 20 
    
    # does weird windows stuff to set wallpaper
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path , 0)


def randomizer(sub_reddits = ["wallpaper","wallpapers"], post_max = 10):
    post_num = random.randrange(1, post_max + 1)
    sub_reddit = sub_reddits[random.randrange(0, len(sub_reddits))]
    
    print(f"Sub Reddit: {sub_reddit}, Post Number: {post_num}")
    return sub_reddit, post_num

def salty_papers(sub_reddits=["wallpapers", "wallpaper"], interval=3600, randomize=False, post_max=10):
    print("SaltyPapers by u/ThePythoneer")

    print(f'Checking: r/{sub_reddits}, Every: {interval} seconds\n')
    while True:
    # Simple loop to make the script update the wallpaper once per hour
        try:
            if randomize:
                sub_reddit, post_num = randomizer(sub_reddits, post_max)
            else:
                sub_reddit = sub_reddits[0]
                post_num = 1

            auth_and_update(sub_reddit, post_num=post_num)
        except:
            print('there was an error retrieving the last wallpaper')
        time.sleep(interval)

if __name__ == '__main__':
    try:
        sub_reddits = list(sys.argv[1])
    except:
        sub_reddits = ['wallpaper', 'wallpapers']
    try:
        interval = int(sys.argv[2])
    except:
        interval = 3600
    salty_papers(sub_reddits=sub_reddits, interval=3600)