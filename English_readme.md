<a name="top"></a>
# Project-pios
Operating system with python. [Switch to Chinese Readme](https://github.com/AccessRetrieved/project-pios/blob/main/README.md)

## Table of contents
1. [Versions](#version)
2. [Installing and executing](#install)
3. [Known Bugs](#bugs)
4. [Images](#images)
***

### Newer than macbook air 2018+ or macbook pro 2018+
PC Users currently not supported

<a name="version"></a>
## Versions
- **Version 4.0.2**
   - Fixed auto-check for update
   - Adjusted browser size
- **Version 4.0.1**
   - Added auto-check for update
   - Can now open apps created by anyone using the given template: app.py
- **Version 4.0**
   - Added email system to Project-Pios
   - Fixed browser's screenshot function
- **Version 3.5.4**
   - Added system controls (BETA)
- **Version 3.5.3**
   - Double click to shutdown
   - Can capture screenshots on webpage (BETA)
- **Version 3.5.2**
   - Quick controls are now accessable in other apps
   - Can now take screenshots in other apps such as settings, browser, and clock
   - Fixed some bugs regarding to auto-switch between wallpapers
- **Version 3.5.1**
   - Added auto-switch wallpaper between light and dark mode
   - Fixed some bugs regarding to Dark Mode
   - Fixed some bugs in Settings.
- **Version 3.5** (Need to reinstall modules: `pip3 install -r r.txt` or `pip install -r r.txt`)
   - Added option for language: English and Chinese
   - Added screenshot function
   - Fixed some bugs
- **Version 3.0** (Need to reinstall modules: `pip3 install -r r.txt` or `pip install -r r.txt`)
   - Added Dark Mode
   - Support real-time switching between dark and light (Need MacOS Big sur - 11.1 or up to switch manually)
   - Added support for user in settings profile.
   - Fixed some bugs
- **Version 2.5** (Need to reinstall modules: `pip3 install -r r.txt` or `pip install -r r.txt`)
   - Added Clock app
   - Can view up to 2 world-wide clocks in the control menu
- **Version 1.5** (Need to reinstall modules: `pip3 install -r r.txt` or `pip install -r r.txt`)
   - Added new bluetooth image
   - Can select wallpaper and change homescreen layout
   - Added Browser
   - Privacy settings are now available in the settings menu
- **Version 1.0**
   - Network
   - Bluetooth
   - Settings

<a name="install"></a>
## Installing an executing
1. [Download](https://www.python.org/ftp/python/3.9.1/python-3.9.1-macosx10.9.pkg) python3.9
2. Open Terminal
3. Run to install homebrew(Copy paste is easier): `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
4. Run:`brew install blueutil`
3. Run:`git clone https://github.com/AccessRetrieved/project-pios`
4. Run:`cd project-pios`
5. Run: `pip3 install -r r.txt` - if errors are generated than run，`pip install -r r.txt`
6. Run: `cd project_pios`
7. Now start the app:`python3 main.py` - if errors are generated than run，`python main.py`

<a name="bugs"></a>
## Known Bugs
1. Switching between dark and light mode needs new resources for bluetooth and wifi
2. Dark mode needs to be added for privacy settings

<a name="images"></a>
## Images
![1](https://i.ibb.co/NLD0sFx/Screen-Shot-2021-01-23-at-1-10-48-PM.png)
![2](https://i.ibb.co/KsKzKpm/Screen-Shot-2021-01-23-at-1-10-52-PM.png)
![3](https://i.ibb.co/gPq0pNW/Screen-Shot-2021-01-23-at-1-10-59-PM.png)
![4](https://i.ibb.co/0XqMJW5/Screen-Shot-2021-01-23-at-1-11-18-PM.png)
![5](https://i.ibb.co/Lp6j161/Screen-Shot-2021-01-23-at-1-11-25-PM.png)
![6](https://i.ibb.co/2N2g648/Screen-Shot-2021-01-23-at-1-11-32-PM.png)
![7](https://i.ibb.co/FqknCvn/Screen-Shot-2021-01-23-at-1-11-36-PM.png)

[Back to top ↑](#top)