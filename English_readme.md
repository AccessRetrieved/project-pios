<a name="top"></a>
# Project-pios
Operating system with python. [Switch to Chinese Readme](https://github.com/AccessRetrieved/project-pios/blob/main/README.md)

## Table of contents
1. [Project-Pios Wiki](https://github.com/AccessRetrieved/Project-Pios/wiki)
2. [Installing and executing](#install)
3. [Known Bugs](#bugs)
4. ['Language'](#language)
5. [Images](#images)
6. [Add-Ons](#helpers)
7. [Versions](#version)
***

### Computers with a small screen not supported
PC Users currently not supported

#### Setup Face Unlock
1. Open Project-Pios
2. Friends > Face ID > Setup

<a name="install"></a>
## Installing an executing
1. [Download](https://www.python.org/ftp/python/3.9.1/python-3.9.1-macosx10.9.pkg) python3.9
2. Open Terminal
3. Run to install homebrew(Copy paste is easier): `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
4. Run:`brew install blueutil`
5. Run: `cd Desktop`
6. Run:`git clone https://github.com/AccessRetrieved/Project-Pios`
7. Run:`cd Project-Pios`
8. Run: `pip3 install -r r.txt` - if errors are generated than run，`pip install -r r.txt`
9. Run: `mv project_pios ..`
10. Run: `cd ..`
11. Run: `rm -rf Project-Pios`
12. Run: `cd project_pios`
13. Now start the app:`python3 main.py` - if errors are generated than run，`python main.py`

<a name="bugs"></a>
## Known Bugs
1. [See](https://github.com/AccessRetrieved/Project-Pios/blob/main/dlib_error_solution.md) Dlib installation error solution
2. Face Recognition temporary supports chinese only
3. ~~Images and icons for dark mode~~

<a name="language"></a>
## Change Language
Change language by changing the language.txt from "zh-cn" to "en".

<a name="images"></a>
## Images
![1](https://i.ibb.co/NLD0sFx/Screen-Shot-2021-01-23-at-1-10-48-PM.png)
![2](https://i.ibb.co/KsKzKpm/Screen-Shot-2021-01-23-at-1-10-52-PM.png)
![3](https://i.ibb.co/gPq0pNW/Screen-Shot-2021-01-23-at-1-10-59-PM.png)
![4](https://i.ibb.co/0XqMJW5/Screen-Shot-2021-01-23-at-1-11-18-PM.png)
![5](https://i.ibb.co/Lp6j161/Screen-Shot-2021-01-23-at-1-11-25-PM.png)
![6](https://i.ibb.co/2N2g648/Screen-Shot-2021-01-23-at-1-11-32-PM.png)
![7](https://i.ibb.co/FqknCvn/Screen-Shot-2021-01-23-at-1-11-36-PM.png)

<a name="helpers"></a>
## Add-Ons
1. [OCR - Optical Characters Recognition](https://github.com/AccessRetrieved/OCR/tree/master)
2. [Qr Code Scanner](https://github.com/AccessRetrieved/Qr-Code-Scanner)

<a name="version"></a>
## Versions
- **Version 5.5**
   - Added gui update
   - Fixed some update bugs
- **Version 5.4**
   - Fixed some known bugs
- **Version 5.3**
   - Added keyboard
   - Fixed some known bugs
- **Version 5.2**
   - Added face recognition for locking Project-Pios
   - Fixed bug for auto-cleaning cache
- **Version 5.1**
   - Reviewed Friends App, screentime usage are available in there
   - Change screentime chart from plt.show() into tkinter figure. (in simulator settings only)
- **Version 5.0**
   - Added screen time record
   - Added system preferences for simulator (Activate by `Command-,`)
- **Version 4.0.8**
   - Added auto-scan qr codes stored in album to check for any contacts
- **Version 4.0.7**
   - Added launch folder: any file put in launch folder will be opened at Project-Pios startup
   - Fixed some bugs
- **Version 4.0.6**
   - Fixed some bugs
- **Version 4.0.5**
   - Added sleep function
   - Rearranged the file system
- **Version 4.0.4**
   - Fixed some bugs
- **Version 4.0.3**
   - Supports two custom apps
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
   - Added system controls with files
- **Version 3.5.3**
   - Double click to shutdown
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

[Back to top ↑](#top)
