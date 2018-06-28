# SaltyPapers 
## by Dalton Pearson
### A python script to update your desktop wallpaper to match the top post on one of the wallpaper sub reddits.
### Tested on Python 3.6

- Usage:
    - Download or clone this repository
    - If you have python installed:
        - run ```pip install -r requirments.txt``` in the repository root
        - then to start the script use ```python main.py```
    - If you don't have python:
        - run main.exe
    - You will be prompted to choose a sub reddit to pull images from, it will default to r/wallpaper if left blank

- To run the script without a cmd prompt window (headless)
    - use ```pythonw main.pyw <subreddit>``` and then you may close the window
    - use ```taskkill /IM pythonw.exe /F``` to end the task

- To run the script at start up
    - Right click ```startup.bat``` and select ```New```  > ```Shortcut```
    - Copy the shortcut
    - In your start menu type ```Run``` press enter
    - Type ```shell:startup``` into your ```Run``` window and press enter
    - Paste the shortcut into the folder
    - All done!
    - You can change the subreddit by editting the last argument in startup.bat