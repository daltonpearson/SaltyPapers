# Salty Papers By: Dalton Pearson
* An application that will keep your desktop wallpaper updated with the top image on a subreddit
## Installation:
    ### Installer:
        * Download the attatched release and double click on ```install.bat``` this will install SaltyPapers and make it run automatically on startup

    ### Manual Installation:
        * Put the dist directory somewhere within your users home directory "C:\%USERPROFILE%" (if you don't put it in your user directory the script will not have the needed privileges to run)
        * Then right-click "SaltyPaper.exe" and left-click "Create Shrotcut"
        * Put the shortcut in "C:\%USERPROFILE%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
        * Now the application should run at Startup

## Settings:
    * The settings can be accessed by right-clicking the system tray icon and left-clicking "Settings", adjust your setting and click "Save Settings"
    * Multiple subreddits can be specified by seperating them by commas
    * Randomize will pick a random post of the top <lowest post rank> of posts, from a random one of the subreddits specified

## Compile From Source:
    * Install the required python packages and make sure that all of the packages are up to date
    * Run ```build.bat```
    * The output files will be located in the ```dist``` folder
## Other:
    * You can also change your settings by editing "salty_papers.config" and then clicking "Refresh" in the tray icon menu
    * Quit closes the app (go figuire), it can be started manually by running SaltyPapers.exe