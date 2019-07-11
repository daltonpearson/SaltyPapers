import pystray
import settings_gui
import salty_papers
import threading
import multiprocessing 
from PIL import Image, ImageDraw
import time
import json
import os
# settings_fp = "./salty_papers.config"
# tray_icon_fp = "./assets/salty-papers-logo.png"
settings_fp ="./salty_papers.config"
tray_icon_fp ="./assets/salty-papers-logo.png"

def setup(icon):
    print(os.getcwd())
    icon.visible = True
    sub_reddits, interval, randomize, post_max = read_config()
    process = multiprocessing.Process(target=salty_papers.salty_papers, args=(sub_reddits, interval, randomize, post_max), daemon=True) 
    process.start()
    all_processes.append(process)
def quit():
    for process in all_processes: 
        process.terminate()
    icon.stop()

def reload():
    for process in all_processes: 
        process.terminate()
    sub_reddits, interval, randomize, post_max = read_config()
    process = multiprocessing.Process(target=salty_papers.salty_papers, args=(sub_reddits, interval, randomize, post_max), daemon=True) 
    process.start()
    all_processes.append(process)

def read_config():
    with open(settings_fp, 'r') as f:
        config = json.load(f)
    return (list(config["sub_reddits"]), int(config["interval"]), bool(config["randomize"]), int(config["post_max"]))

def settings_click():
    process = multiprocessing.Process(target=settings_gui.settings_gui, args=(settings_fp,))
    process.start()
    all_processes.append(process)
    while(process.is_alive()==True):
        time.sleep(1)
    reload()

def main():
    global all_processes, icon
    multiprocessing.freeze_support()
    all_processes = []
    icon = pystray.Icon('test name', 
        Image.open(tray_icon_fp), 
        menu=pystray.Menu(
            pystray.MenuItem(
                'Quit',
                quit),
            pystray.MenuItem(
                'Refresh',
                reload),
            pystray.MenuItem(
                'Settings',
                
                settings_click),))

    icon.run(setup=setup)

if __name__ == '__main__':
    main()
    # multiprocessing.freeze_support()
    # all_processes = []
    # setting_process = None
    # icon = pystray.Icon('test name', 
    #     Image.open(tray_icon_fp), 
    #     menu=pystray.Menu(
    #         pystray.MenuItem(
    #             'Quit',
    #             quit),
    #         pystray.MenuItem(
    #             'Refresh',
    #             reload),
    #         pystray.MenuItem(
    #             'Settings',
    #             settings_click),))

    # icon.run(setup=setup)

