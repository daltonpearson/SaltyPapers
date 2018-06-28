import requests
import time
import urllib.request
import ctypes
import os

CLIENT_ID = 'AERmPCqvfBEALQ'
CLIENT_SECRET = 'mMm2fM63jX1onIXN-0bkdwUDXzk'


def auth_and_update():
    client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    post_data = {"grant_type": "client_credentials", "grant_type":"client_credentials"}
    headers = {"User-Agent": "SaltyPapers/0.1 by ThePythoneer"}
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
    
    response_header = response.json()

    headers = {"Authorization": f"bearer {response_header['access_token']}", "User-Agent": "SaltyPapers/0.1 by ThePythoneer"}
    response = requests.get(f"https://oauth.reddit.com/r/{SUB_REDDIT}/.json?limit=1", headers=headers)
    response = response.json()['data']['children'][0]['data']
    img_url = response['preview']['images'][0]['source']['url']
    img_title = response['title']
    print(f'Current Wallpaper: {img_title}\n')    

    #saves image at link to file
    urllib.request.urlretrieve(img_url, f'reddit_wallpaper.jpeg')

    path = os.path.abspath("reddit_wallpaper.jpeg")
    SPI_SETDESKWALLPAPER = 20 

    # does weird windows stuff to set wallpaper
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path , 0)

if __name__ == '__main__':
    print("SaltyPapers by u/ThePythoneer")
    SUB_REDDIT = input('What subreddit would you like to use (defaults to "wallpaper" if blank):\n').split("/")[-1] or 'wallpaper'
    print(f'Using: r/{SUB_REDDIT}\n')
    while True:
    # Simple loop to make the script update the wallpaper once per hour
        try:
            auth_and_update()
        except:
            print('there was an error retrieving the last wallpaper')
        time.sleep(3600)