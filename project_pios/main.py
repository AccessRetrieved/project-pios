from tkinter import *
from tkinter import ttk
from tkinter import simpledialog, messagebox
from datetime import datetime
from PIL import Image, ImageTk
import requests
import os
import tkmacosx
import platform
import socket
import re
import uuid
import psutil
import webview
import sys
import shutil
import arrow
import webbrowser
import pyscreenshot
import yagmail
from app import import_app, quit_app # Add custom app here
from app2 import import_app2, quit_app2 # Add second custom app here
import objc #Add this to github to make it look better

#change all path from "/FILE" to "/FILE" for github

# Custom App Icons
NSCustomAppIcon1 = os.getcwd() + '/app1.png'
NSCustomAppIcon2 = os.getcwd() + '/app2.png'

root = Tk()
root.geometry('400x800')
root.title('')
#root.config(cursor='none')
#root.tk.call("::tk::unsupported::MacWindowStyle", "style", root._w, "plain", "none")
root.resizable(0, 0)

##################################
#                                #
#                                #
# P R O J E C T    V E R S I O N #
#                                #
#                                #
##################################
###############################################
NSLocalVersion = StringVar()                  #
#                                             #
# U P D A T E   T H I S   E V E R Y T I M E ! #
#                                             #
NSLocalVersion.set('4.0.2')                     #
###############################################
##################################
#                                #
#                                #
# P R O J E C T    V E R S I O N #
#                                #
#                                #
##################################

dark_theme = {
    "bg": "black",
    "fg": "white"
}

theme = {
    "bg": "white",
    "fg": "black"
}

NSWifiValue = IntVar()
NSWifiCount = 0
os.system('networksetup -setairportpower en0 on')
with open(os.getcwd() + '/system/wifi/bool.txt', 'w') as file:
    file.truncate(0)
    file.write('true')

NSDarkModeStat = IntVar()
NSAutoSwitchWallpaperStat = IntVar()

NSSettingsFrame = IntVar()

NSUpdateAlert = 0

NSLanguageValue = StringVar()
try:
    with open(os.getcwd() + '/language.txt', 'r') as file:
        if file.read() == 'en':
            NSLanguageValue.set('en')
            pass
        elif file.read() == 'en\n':
            NSLanguageValue.set('en')
            pass
        elif file.read() == 'zh-cn':
            NSLanguageValue.set('zh-cn')
        elif file.read() == 'zh-cn\n':
            NSLanguageValue.set('zh-cn')
            pass
except:
    NSLanguageValue.set('en')

NSBluetoothValue = IntVar()
NSBluetoothCount = 0
response = os.popen('blueutil -p').read()
if response == '1\n':
    NSBluetoothValue.set(1)
    with open(os.getcwd() + '/system/wifi/bool.txt', 'w') as file:
        file.truncate(0)
        file.write('true')
        pass
else:
    NSBluetoothValue.set(0)
    with open(os.getcwd() + '/system/wifi/bool.txt', 'w') as file:
        file.truncate(0)
        file.write('false')
        pass

NSMenuCounter = 1
NSAutoSwitchCounter = 1

NSBrowserSearchEngine = IntVar()
NSBrowserSearchEngine.set(0)

def update_time():
    orig = str(datetime.now())
    fil = orig[11:16]
    ampm = fil[0:2]
    if int(ampm) > 12:
        time = '{}{} PM'.format(int(ampm) - 12, fil[2:])
        NSDisplayTime['text'] = time
    else:
        NSDisplayTime['text'] = '{} AM'.format(fil)

    root.after(ms=1000, func=update_time)

def update_date():
    date = datetime.today()
    fil = date.strftime('%b') + ' ' + date.strftime('%d') + ' ' + date.strftime('%a')
    NSDisplayDate['text'] = fil
    root.after(ms=1000, func=update_date)

def update_wifi():
    timeout = 5
    url = 'http://google.com'
    try:
        response = requests.get(url, timeout=timeout)
        pic = Image.open(os.getcwd() + '/wifi.png')
        pic = pic.resize((25, 25), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(pic)
        NSSignalWidget.config(image = img)
        NSSignalWidget.image = img
        NSWifiValue.set(1)
    except:
        NSSignalWidget.config(image = '')
        NSSignalWidget.image = ''
        NSWifiValue.set(0)

    root.after(ms=3000, func=update_wifi)

def update_bluetooth():
    status = os.popen('blueutil -p').read()
    
    if status == '1\n':
        bimg = Image.open(os.getcwd() + '/bluetooth.png')
        bimg = bimg.resize((15, 15), Image.ANTIALIAS)
        bpic = ImageTk.PhotoImage(bimg)
        NSBlueSignalWidget.config(image = bpic)
        NSBlueSignalWidget.image = bpic
        NSBluetoothValue.set(1)
    else:
        NSBlueSignalWidget.config(image='')
        NSBlueSignalWidget.image = ''
        NSBluetoothValue.set(0)

    root.after(ms=3000, func=update_bluetooth)

def pulldown_menu(event):
    global NSMenuCounter
    NSMenuCounter += 1

    def change_language():
        if NSLanguageValue.get() == 'en':
            NSWifiLabel['text'] = 'Wifi'
            NSBluetoothLabel['text'] = 'Bluetooth'
            NSShutdownLabel['text'] = 'Shutdown'
            NSWallpaperLabel['text'] = 'Wallpaper'
            NSClockLabel['text'] = 'Clock'
            NSScreenshotLabel['text'] = 'Screenshot'
            pass
        else:
            NSWifiLabel['text'] = '网络'
            NSBluetoothLabel['text'] = '蓝牙'
            NSShutdownLabel['text'] = '关机'
            NSWallpaperLabel['text'] = '壁纸'
            NSClockLabel['text'] = '时间'
            NSScreenshotLabel['text'] = '截屏'
            pass

        NSCanvas.after(ms=1000, func=change_language)

    change_language()

    if NSMenuCounter % 2 == 0:
        NSCanvas['bg'] = '#4d4d4d'
        NSControlMenu.place(relx=0.5, rely=0.2125, anchor=CENTER)

        NSWifiControl.place(relx=0.1, rely=0.1, anchor=CENTER)
        NSWifiLabel.place(relx=0.1, rely=0.2, anchor=CENTER)

        NSBluetoothControl.place(relx=0.3, rely=0.1, anchor=CENTER)
        NSBluetoothLabel.place(relx=0.3, rely=0.2, anchor=CENTER)

        NSShutdownControl.place(relx=0.5, rely=0.1, anchor=CENTER)
        NSShutdownLabel.place(relx=0.5, rely=0.2, anchor=CENTER)

        NSWallpaperControl.place(relx=0.7, rely=0.1, anchor=CENTER)
        NSWallpaperLabel.place(relx=0.7, rely=0.2, anchor=CENTER)

        NSClockControl.place(relx=0.9, rely=0.1, anchor=CENTER)
        NSClockLabel.place(relx=0.9, rely=0.2, anchor=CENTER)

        NSScreenshotControl.place(relx=0.1, rely=0.4, anchor=CENTER)
        NSScreenshotLabel.place(relx=0.1, rely=0.5, anchor=CENTER)

        if NSWifiValue.get() == 1:
            NSWifiControl['bg'] = '#1b73e9'
        else:
            NSWifiControl['bg'] = '#dcdcdc'

        if NSBluetoothValue.get() == 1:
            NSBluetoothControl['bg'] = '#1b73e9'
        elif NSBluetoothValue.get() != 1:
            NSBluetoothControl['bg'] = '#dcdcdc'
    else:
        NSWifiControl.place_forget()
        NSWifiLabel.place_forget()
        NSBluetoothControl.place_forget()
        NSBluetoothLabel.place_forget()
        NSShutdownControl.place_forget()
        NSShutdownLabel.place_forget()
        NSWallpaperControl.place_forget()
        NSWallpaperLabel.place_forget()
        NSClockControl.place_forget()
        NSClockLabel.place_forget()
        NSControlMenu.place_forget()
        NSScreenshotControl.place_forget()
        NSScreenshotLabel.place_forget()
        pass

def manage_wifi():
    global NSWifiCount
    NSWifiCount += 1
    if NSWifiCount % 2 == 0:
        os.system('networksetup -setairportpower en0 on')
        NSWifiValue.set(1)
        NSWifiControl['bg'] = '#1b73e9'
        with open(os.getcwd() + '/system/wifi/bool.txt', 'w') as file:
            file.truncate(0)
            file.write('true')
    else:
        os.system('networksetup -setairportpower en0 off')
        NSWifiValue.set(0)
        NSWifiControl['bg'] = '#dcdcdc'
        with open(os.getcwd() + '/system/wifi/bool.txt', 'w') as file:
            file.truncate(0)
            file.write('false')

def manage_bluetooth():
    global NSBluetoothCount
    NSBluetoothCount += 1
    if NSBluetoothCount % 2 == 0:
        os.system('blueutil -p on')
        NSBluetoothControl['bg'] = '#1b73e9'
        NSBluetoothValue.set(1)
        with open(os.getcwd() + '/system/bluetooth/bool.txt', 'w') as file:
            file.truncate(0)
            file.write('true')
    else:
        os.system('blueutil -p off')
        NSBluetoothControl['bg'] = '#dcdcdc'
        NSBluetoothValue.set(0)
        with open(os.getcwd() + '/system/bluetooth/bool.txt', 'w') as file:
            file.truncate(0)
            file.write('false')

def clicked(event):
    print('true')

def return_home(event):
    NSSettingsFrame.set(0)
    NSWifiControl.place_forget()
    NSWifiLabel.place_forget()
    NSBluetoothControl.place_forget()
    NSBluetoothLabel.place_forget()
    NSShutdownControl.place_forget()
    NSShutdownLabel.place_forget()
    NSWallpaperControl.place_forget()
    NSWallpaperLabel.place_forget()
    NSClockControl.place_forget()
    NSClockLabel.place_forget()
    NSScreenshotControl.place_forget()
    NSScreenshotLabel.place_forget()
    NSControlMenu.place_forget()

    destroy_apps()
    
    try:
        quit_app()
    except:
        pass
    try:
        quit_app2()
    except:
        pass

    add_apps()

def settings(event):
    global NSSettingsView
    NSSettingsView = Frame(NSWallpaper)
    NSSettingsView.pack(fill=BOTH, expand=True)

    NSSettingsView.bind('<Button-1>', takedown_pulldown_menu)

    remove_apps()

    def about_this_mac():
        machine_platform = '机器: ' + platform.machine()
        machine_system = '系统: ' + platform.system()
        machine_processor = '芯片: ' + platform.processor()
        machine_ip = 'IP: ' + socket.gethostbyname(socket.gethostname())
        machine_hostname = '网络名称: ' + socket.gethostname()
        machine_mac = 'MAC: ' + ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        machine_ram = '缓存: ' + str(round(psutil.virtual_memory().total / (1024.0 **3))) + ' GB'

        def close_about():
            NSSettingsFrame.set(0)
            NSSettingsView['bg'] = 'white'
            NSSettingsSearchEngine.place(relx=0.5, rely=0.2, anchor=CENTER)
            NSSettingsWallpaper.place(relx=0.5, rely=0.27, anchor=CENTER)
            NSSettingsPrivacy.place(relx=0.5, rely=0.34, anchor=CENTER)
            NSSettingsAbout.place(relx=0.5, rely=0.41, anchor=CENTER)
            NSSettingsProfile.place(relx=0.5, rely=0.1, anchor=CENTER)

            NSPopupAlert.destroy()

        NSSettingsProfile.place_forget()
        NSSettingsSearchEngine.place_forget()
        NSSettingsWallpaper.place_forget()
        NSSettingsPrivacy.place_forget()
        NSSettingsAbout.place_forget()
        NSSettingsView['bg'] = '#b3b3b3'

        NSPopupAlert = Frame(NSSettingsView, width=380, height=300)
        NSPopupAlert.place(relx=0.5, rely=0.5, anchor=CENTER)

        NSPopupTitle = Label(NSPopupAlert, text='关于本机: ', fg='#949494', font=("Futura", 20))
        NSPopupTitle.place(relx=0.135, rely=0.05, anchor=CENTER)

        NSPlatform = Label(NSPopupAlert, text=machine_platform, font=("Futura", 12))
        NSSystem = Label(NSPopupAlert, text=machine_system, font=("Futura", 12))
        NSProcessor = Label(NSPopupAlert, text=machine_processor, font=("Futura", 12))
        NSip = Label(NSPopupAlert, text=machine_ip, font=("Futura", 12))
        NSHostname = Label(NSPopupAlert, text=machine_hostname, font=("Futura", 12))
        NSMac = Label(NSPopupAlert, text=machine_mac, font=("Futura", 12))
        NSRam = Label(NSPopupAlert, text=machine_ram, font=("Futura", 12))
        NSDisplayVersion = Label(NSPopupAlert, text='版本: ' + NSLocalVersion.get(), font=("Futura", 12))

        NSPlatform.place(relx=0.5, rely=0.1, anchor=CENTER)
        NSSystem.place(relx=0.5, rely=0.2, anchor=CENTER)
        NSProcessor.place(relx=0.5, rely=0.3, anchor=CENTER)
        NSip.place(relx=0.5, rely=0.4, anchor=CENTER)
        NSHostname.place(relx=0.5, rely=0.5, anchor=CENTER)
        NSMac.place(relx=0.5, rely=0.6, anchor=CENTER)
        NSRam.place(relx=0.5, rely=0.7, anchor=CENTER)
        NSDisplayVersion.place(relx=0.5, rely=0.8, anchor=CENTER)

        NSPopupAlertClose = tkmacosx.Button(NSPopupAlert, text='关闭', bg='white', fg='black', font=("Futura", 15), borderless=1, activebackground='white', activeforeground='black', command=close_about)
        NSPopupAlertClose.place(relx=0.5, rely=0.9, anchor=CENTER)

    def choose_search_engine():
        NSSettingsFrame.set(1)
        NSSettingsView['bg'] = '#b3b3b3'

        NSSettingsProfile.place_forget()
        NSSettingsSearchEngine.place_forget()
        NSSettingsWallpaper.place_forget()
        NSSettingsPrivacy.place_forget()
        NSSettingsAbout.place_forget()

        def close_popup():
            if NSBrowserSearchEngineBox.get() == 'Google':
                NSBrowserSearchEngine.set(0)
                NSSettingsFrame.set(0)
                NSSettingsView['bg'] = 'white'
                NSSettingsProfile.place(relx=0.5, rely=0.1, anchor=CENTER)
                NSSettingsSearchEngine.place(relx=0.5, rely=0.2, anchor=CENTER)
                NSSettingsWallpaper.place(relx=0.5, rely=0.27, anchor=CENTER)
                NSSettingsPrivacy.place(relx=0.5, rely=0.34, anchor=CENTER)
                NSSettingsAbout.place(relx=0.5, rely=0.41, anchor=CENTER)
                NSSettingsProfile.place(relx=0.5, rely=0.1, anchor=CENTER)

                NSPopupAlert.destroy()
            else:
                NSBrowserSearchEngine.set(1)
                NSSettingsFrame.set(0)
                NSSettingsView['bg'] = 'white'
                NSSettingsSearchEngine.place(relx=0.5, rely=0.2, anchor=CENTER)
                NSSettingsWallpaper.place(relx=0.5, rely=0.27, anchor=CENTER)
                NSSettingsPrivacy.place(relx=0.5, rely=0.34, anchor=CENTER)
                NSSettingsAbout.place(relx=0.5, rely=0.41, anchor=CENTER)
                NSSettingsProfile.place(relx=0.5, rely=0.1, anchor=CENTER)

                NSPopupAlert.destroy()

        def change_language():
            if NSLanguageValue.get() == 'en':
                NSSettingsProfile['text'] = '    Jerry Hu'
                NSSettingsSearchEngine['text'] = 'Browser'
                NSSettingsWallpaper['text'] = 'Wallpaper'
                NSSettingsPrivacy['text'] = 'Privacy'
                NSSettingsAbout['text'] = 'About'
                pass
            else:
                NSSettingsProfile['text'] = '    胡家睿'
                NSSettingsWallpaper['text'] = '壁纸'
                NSSettingsPrivacy['text'] = '隐私'
                NSSettingsAbout['text'] = '关于本机'

                pass

            NSSettingsView.after(ms=1, func=change_language)

        NSPopupAlert = Frame(NSSettingsView, width=380, height=300)
        NSPopupAlert.place(relx=0.5, rely=0.5, anchor=CENTER)

        NSPopupTitle = Label(NSPopupAlert, text='选择浏览器: ', fg='#949494', font=("Futura", 20))
        NSPopupTitle.place(relx=0.17, rely=0.05, anchor=CENTER)

        NSBrowserSearchEngineBox = ttk.Combobox(NSPopupAlert, value=['Google', '百度'])
        NSBrowserSearchEngineBox.place(relx=0.5, rely=0.4, anchor=CENTER)
        if NSBrowserSearchEngine.get() == 0:
            NSBrowserSearchEngineBox.current(0)
        else:
            NSBrowserSearchEngineBox.current(1)

        NSPopupAlertClose = tkmacosx.Button(NSPopupAlert, text='关闭', bg='white', fg='black', font=("Futura", 15), borderless=1, activebackground='white', activeforeground='black', command=close_popup)
        NSPopupAlertClose.place(relx=0.5, rely=0.85, anchor=CENTER)

        change_language()

    def choose_wallpaper():
        NSSettingsFrame.set(1)
        NSSettingsView['bg'] = '#b3b3b3'
        NSSettingsProfile.place_forget()
        NSSettingsSearchEngine.place_forget()
        NSSettingsWallpaper.place_forget()
        NSSettingsPrivacy.place_forget()
        NSSettingsAbout.place_forget()

        def close_popup():
            NSSettingsFrame.set(1)
            NSSettingsView['bg'] = 'white'
            NSSettingsSearchEngine.place(relx=0.5, rely=0.2, anchor=CENTER)
            NSSettingsWallpaper.place(relx=0.5, rely=0.27, anchor=CENTER)
            NSSettingsPrivacy.place(relx=0.5, rely=0.34, anchor=CENTER)
            NSSettingsAbout.place(relx=0.5, rely=0.41, anchor=CENTER)
            NSSettingsProfile.place(relx=0.5, rely=0.1, anchor=CENTER)

            NSPopupAlert.destroy()

        def change_language():
            if NSLanguageValue.get() == 'en':
                NSSettingsProfile['text'] = '    Jerry Hu'
                NSSettingsSearchEngine['text'] = 'Browser'
                NSSettingsWallpaper['text'] = 'Wallpaper'
                NSSettingsPrivacy['text'] = 'Privacy'
                NSSettingsAbout['text'] = 'About'
                pass
            else:
                NSSettingsProfile['text'] = '    胡家睿'
                NSSettingsWallpaper['text'] = '壁纸'
                NSSettingsPrivacy['text'] = '隐私'
                NSSettingsAbout['text'] = '关于本机'
                pass

            NSSettingsView.after(ms=1, func=change_language)

        NSPopupAlert = Frame(NSSettingsView, width=380, height=400)
        NSPopupAlert.place(relx=0.5, rely=0.5, anchor=CENTER)

        NSPopupTitle = Label(NSPopupAlert, text='选择壁纸: ', fg='#949494', font=("Futura", 20))
        NSPopupTitle.place(relx=0.17, rely=0.05, anchor=CENTER)

        def w1(event):
            img = Image.open(os.getcwd() + '/wallpaper/1.jpg')
            shutil.copy(src=os.getcwd() + '/wallpaper/1.jpg', dst=os.getcwd() + '/wallpaper.jpg')
            pic = ImageTk.PhotoImage(img)
            NSWallpaper.config(image = pic)
            NSWallpaper.image = pic
        def w2(event):
            img = Image.open(os.getcwd() + '/wallpaper/2.jpg')
            shutil.copy(src=os.getcwd() + '/wallpaper/2.jpg', dst=os.getcwd() + '/wallpaper.jpg')
            pic = ImageTk.PhotoImage(img)
            NSWallpaper.config(image = pic)
            NSWallpaper.image = pic
        def w3(event):
            img = Image.open(os.getcwd() + '/wallpaper/3.jpg')
            shutil.copy(src=os.getcwd() + '/wallpaper/3.jpg', dst=os.getcwd() + '/wallpaper.jpg')
            pic = ImageTk.PhotoImage(img)
            NSWallpaper.config(image = pic)
            NSWallpaper.image = pic
        def w4(event):
            img = Image.open(os.getcwd() + '/wallpaper/4.jpg')
            shutil.copy(src=os.getcwd() + '/wallpaper/4.jpg', dst=os.getcwd() + '/wallpaper.jpg')
            pic = ImageTk.PhotoImage(img)
            NSWallpaper.config(image = pic)
            NSWallpaper.image = pic
        def w5(event):
            img = Image.open(os.getcwd() + '/wallpaper/5.jpg')
            shutil.copy(src=os.getcwd() + '/wallpaper/5.jpg', dst=os.getcwd() + '/wallpaper.jpg')
            pic = ImageTk.PhotoImage(img)
            NSWallpaper.config(image = pic)
            NSWallpaper.image = pic
        def w6(event):
            img = Image.open(os.getcwd() + '/wallpaper/6.jpg')
            shutil.copy(src=os.getcwd() + '/wallpaper/6.jpg', dst=os.getcwd() + '/wallpaper.jpg')
            pic = ImageTk.PhotoImage(img)
            NSWallpaper.config(image = pic)
            NSWallpaper.image = pic
        def w7(event):
            img = Image.open(os.getcwd() + '/wallpaper/7.jpg')
            shutil.copy(src=os.getcwd() + '/wallpaper/7.jpg', dst=os.getcwd() + '/wallpaper.jpg')
            pic = ImageTk.PhotoImage(img)
            NSWallpaper.config(image = pic)
            NSWallpaper.image = pic
        def w8(event):
            img = Image.open(os.getcwd() + '/wallpaper/8.jpg')
            shutil.copy(src=os.getcwd() + '/wallpaper/8.jpg', dst=os.getcwd() + '/wallpaper.jpg')
            pic = ImageTk.PhotoImage(img)
            NSWallpaper.config(image = pic)
            NSWallpaper.image = pic
        def w9(event):
            img = Image.open(os.getcwd() + '/wallpaper/9.jpg')
            shutil.copy(src=os.getcwd() + '/wallpaper/9.jpg', dst=os.getcwd() + '/wallpaper.jpg')
            pic = ImageTk.PhotoImage(img)
            NSWallpaper.config(image = pic)
            NSWallpaper.image = pic
        def w10(event):
            img = Image.open(os.getcwd() + '/wallpaper/10.jpg')
            shutil.copy(src=os.getcwd() + '/wallpaper/10.jpg', dst=os.getcwd() + '/wallpaper.jpg')
            pic = ImageTk.PhotoImage(img)
            NSWallpaper.config(image = pic)
            NSWallpaper.image = pic

        wall1img = Image.open(os.getcwd() + '/wallpaper/1.jpg')
        wall2img = Image.open(os.getcwd() + '/wallpaper/2.jpg')
        wall3img = Image.open(os.getcwd() + '/wallpaper/3.jpg')
        wall4img = Image.open(os.getcwd() + '/wallpaper/4.jpg')
        wall5img = Image.open(os.getcwd() + '/wallpaper/5.jpg')
        wall6img = Image.open(os.getcwd() + '/wallpaper/6.jpg')
        wall7img = Image.open(os.getcwd() + '/wallpaper/7.jpg')
        wall8img = Image.open(os.getcwd() + '/wallpaper/8.jpg')
        wall9img = Image.open(os.getcwd() + '/wallpaper/9.jpg')
        wall10img = Image.open(os.getcwd() + '/wallpaper/10.jpg')
        wall1img = wall1img.resize((40, 70), Image.ANTIALIAS)
        wall2img = wall2img.resize((40, 70), Image.ANTIALIAS)
        wall3img = wall3img.resize((40, 70), Image.ANTIALIAS)
        wall4img = wall4img.resize((40, 70), Image.ANTIALIAS)
        wall5img = wall5img.resize((40, 70), Image.ANTIALIAS)
        wall6img = wall6img.resize((40, 70), Image.ANTIALIAS)
        wall7img = wall7img.resize((40, 70), Image.ANTIALIAS)
        wall8img = wall8img.resize((40, 70), Image.ANTIALIAS)
        wall9img = wall9img.resize((40, 70), Image.ANTIALIAS)
        wall10img = wall10img.resize((40, 70), Image.ANTIALIAS)
        wall1pic = ImageTk.PhotoImage(wall1img)
        wall2pic = ImageTk.PhotoImage(wall2img)
        wall3pic = ImageTk.PhotoImage(wall3img)
        wall4pic = ImageTk.PhotoImage(wall4img)
        wall5pic = ImageTk.PhotoImage(wall5img)
        wall6pic = ImageTk.PhotoImage(wall6img)
        wall7pic = ImageTk.PhotoImage(wall7img)
        wall8pic = ImageTk.PhotoImage(wall8img)
        wall9pic = ImageTk.PhotoImage(wall9img)
        wall10pic = ImageTk.PhotoImage(wall10img)
        wall1 = Label(NSPopupAlert, text='', image=wall1pic)
        wall2 = Label(NSPopupAlert, text='', image=wall2pic)
        wall3 = Label(NSPopupAlert, text='', image=wall3pic)
        wall4 = Label(NSPopupAlert, text='', image=wall4pic)
        wall5 = Label(NSPopupAlert, text='', image=wall5pic)
        wall6 = Label(NSPopupAlert, text='', image=wall6pic)
        wall7 = Label(NSPopupAlert, text='', image=wall7pic)
        wall8 = Label(NSPopupAlert, text='', image=wall8pic)
        wall9 = Label(NSPopupAlert, text='', image=wall9pic)
        wall10 = Label(NSPopupAlert, text='', image=wall10pic)
        wall1.image = wall1pic
        wall2.image = wall2pic
        wall3.image = wall3pic
        wall4.image = wall4pic
        wall5.image = wall5pic
        wall6.image = wall6pic
        wall7.image = wall7pic
        wall8.image = wall8pic
        wall9.image = wall9pic
        wall10.image = wall10pic
        wall1.place(relx=0.15, rely=0.25, anchor=CENTER)
        wall2.place(relx=0.3, rely=0.25, anchor=CENTER)
        wall3.place(relx=0.45, rely=0.25, anchor=CENTER)
        wall4.place(relx=0.6, rely=0.25, anchor=CENTER)
        wall5.place(relx=0.75, rely=0.25, anchor=CENTER)
        wall6.place(relx=0.9, rely=0.25, anchor=CENTER)
        wall7.place(relx=0.15, rely=0.5, anchor=CENTER)
        wall8.place(relx=0.3, rely=0.5, anchor=CENTER)
        wall9.place(relx=0.45, rely=0.5, anchor=CENTER)
        wall10.place(relx=0.6, rely=0.5, anchor=CENTER)
        wall1.bind('<Button-1>', w1)
        wall2.bind('<Button-1>', w2)
        wall3.bind('<Button-1>', w3)
        wall4.bind('<Button-1>', w4)
        wall5.bind('<Button-1>', w5)
        wall6.bind('<Button-1>', w6)
        wall7.bind('<Button-1>', w7)
        wall8.bind('<Button-1>', w8)
        wall9.bind('<Button-1>', w9)
        wall10.bind('<Button-1>', w10)

        NSPopupAlertClose = tkmacosx.Button(NSPopupAlert, text='关闭', bg='white', fg='black', font=("Futura", 15), borderless=1, activebackground='white', activeforeground='black', command=close_popup)
        NSPopupAlertClose.place(relx=0.5, rely=0.85, anchor=CENTER)

        change_language()

    def privacy():
        NSSettingsFrame.set(1)
        NSSettingsView['bg'] = '#b3b3b3'
        NSSettingsProfile.place_forget()
        NSSettingsSearchEngine.place_forget()
        NSSettingsWallpaper.place_forget()
        NSSettingsPrivacy.place_forget()
        NSSettingsAbout.place_forget()

        def close_popup():
            NSSettingsFrame.set(0)
            NSSettingsView['bg'] = 'white'
            NSSettingsSearchEngine.place(relx=0.5, rely=0.2, anchor=CENTER)
            NSSettingsWallpaper.place(relx=0.5, rely=0.27, anchor=CENTER)
            NSSettingsPrivacy.place(relx=0.5, rely=0.34, anchor=CENTER)
            NSSettingsAbout.place(relx=0.5, rely=0.41, anchor=CENTER)
            NSSettingsProfile.place(relx=0.5, rely=0.1, anchor=CENTER)

            NSPopupAlert.destroy()

        def change_language():
            if NSLanguageValue.get() == 'en':
                NSSettingsProfile['text'] = '    Jerry Hu'
                NSSettingsSearchEngine['text'] = 'Browser'
                NSSettingsWallpaper['text'] = 'Wallpaper'
                NSSettingsPrivacy['text'] = 'Privacy'
                NSSettingsAbout['text'] = 'About'
                pass
            else:
                NSSettingsProfile['text'] = '    胡家睿'
                NSSettingsWallpaper['text'] = '壁纸'
                NSSettingsPrivacy['text'] = '隐私'
                NSSettingsAbout['text'] = '关于本机'
                pass

                NSSettingsView.after(ms=1, func=change_language)

        NSPopupAlert = Frame(NSSettingsView, width=380, height=400)
        NSPopupAlert.place(relx=0.5, rely=0.5, anchor=CENTER)

        NSPopupTitle = Label(NSPopupAlert, text='隐私: ', fg='#949494', font=("Futura", 20))
        NSPopupTitle.place(relx=0.1, rely=0.05, anchor=CENTER)

        NSPopupBody = Label(NSPopupAlert, text='Project-Pios 将获得通知，麦克风，和照相机权限。\n 您可以在macos设置中选择关闭或开启。部分系统报告\n会自动发送给软件开发者。', font=("Futura", 15))
        NSPopupBody.place(relx=0.5, rely=0.45, anchor=CENTER)

        NSPopupClose = tkmacosx.Button(NSPopupAlert, text='关闭', font=("Futura", 12), borderless=1, activeforeground='black', activebackground='white', command=close_popup)
        NSPopupClose.place(relx=0.5, rely=0.85, anchor=CENTER)

        change_language()

    def change_mode():
        if NSDarkModeStat.get() == 1:
            if NSSettingsFrame.get() == 1:
                pass
            else:
                NSSettingsView.config(bg=dark_theme['bg'])
                pass

            NSSettingsSearchEngine['bg'] = dark_theme['bg']
            NSSettingsSearchEngine['fg'] = dark_theme['fg']
            NSSettingsWallpaper['bg'] = dark_theme['bg']
            NSSettingsWallpaper['fg'] = dark_theme['fg']
            NSSettingsPrivacy['bg'] = dark_theme['bg']
            NSSettingsPrivacy['fg'] = dark_theme['fg']
            NSSettingsAbout['bg'] = dark_theme['bg']
            NSSettingsAbout['fg'] = dark_theme['fg']
            pass
        else:
            if NSSettingsFrame.get() == 1:
                pass
            else:
                NSSettingsView.config(bg=theme['bg'])
                pass

            NSSettingsSearchEngine['bg'] = theme['bg']
            NSSettingsSearchEngine['fg'] = theme['fg']
            NSSettingsWallpaper['bg'] = theme['bg']
            NSSettingsWallpaper['fg'] = theme['fg']
            NSSettingsPrivacy['bg'] = theme['bg']
            NSSettingsPrivacy['fg'] = theme['fg']
            NSSettingsAbout['bg'] = theme['bg']
            NSSettingsAbout['fg'] = theme['fg']
            pass

        NSSettingsView.after(ms=10, func=change_mode)

    def open_page():
        webbrowser.open('https://github.com/AccessRetrieved/project-pios')

    def change_language():
        if NSLanguageValue.get() == 'en':
            NSSettingsProfile['text'] = '    Jerry Hu'
            NSSettingsSearchEngine['text'] = 'Browser'
            NSSettingsWallpaper['text'] = 'Wallpaper'
            NSSettingsPrivacy['text'] = 'Privacy'
            NSSettingsAbout['text'] = 'About'
            pass
        else:
            NSSettingsProfile['text'] = '    胡家睿'
            NSSettingsSearchEngine['text'] = '浏览器'
            NSSettingsWallpaper['text'] = '壁纸'
            NSSettingsPrivacy['text'] = '隐私'
            NSSettingsAbout['text'] = '关于本机'
            pass

        NSSettingsView.after(ms=1000, func=change_language)

    NSSettingsProfileimg = Image.open(os.getcwd() + '/profile.png')
    NSSettingsProfileimg = NSSettingsProfileimg.resize((50, 50), Image.ANTIALIAS)
    NSSettingsProfilepic = ImageTk.PhotoImage(NSSettingsProfileimg)

    NSSettingsProfile = tkmacosx.Button(NSSettingsView, text='    胡家睿', borderless=1, font=("Futura", 20), height=80, width=400, activebackground='white', activeforeground='black', image=NSSettingsProfilepic, compound=LEFT, command=open_page)
    NSSettingsProfile.image = NSSettingsProfilepic
    NSSettingsProfile.place(relx=0.5, rely=0.1, anchor=CENTER)

    NSSettingsSearchEngine = tkmacosx.Button(NSSettingsView, text='浏览器', borderless=1, font=("Futura", 15), height=50, width=400, activebackground='white', activeforeground='black', command=choose_search_engine)
    NSSettingsSearchEngine.place(relx=0.5, rely=0.2, anchor=CENTER)

    NSSettingsWallpaper = tkmacosx.Button(NSSettingsView, text='壁纸', borderless=1, font=("Futura", 15), height=50, width=400, activebackground='white', activeforeground='black', command=choose_wallpaper)
    NSSettingsWallpaper.place(relx=0.5, rely=0.27, anchor=CENTER)

    NSSettingsPrivacy = tkmacosx.Button(NSSettingsView, text='隐私', borderless=1, font=("Futura", 15), height=50, width=400, activebackground='white', activeforeground='black', command=privacy)
    NSSettingsPrivacy.place(relx=0.5, rely=0.34, anchor=CENTER)

    NSSettingsAbout = tkmacosx.Button(NSSettingsView, text='关于本机', borderless=1, font=("Futura", 15), height=50, width=400, activebackground='white', activeforeground='black', command=about_this_mac)
    NSSettingsAbout.place(relx=0.5, rely=0.41, anchor=CENTER)

    change_mode()
    change_language()

def browser(event):
    global NSBrowserView
    NSBrowserView = Frame(NSWallpaper)
    NSBrowserView.pack(fill=BOTH, expand=True)

    NSBrowserView.bind('<Button-1>', takedown_pulldown_menu)

    remove_apps()

    def on(event):
        NSBrowserURLQuery.delete(0, END)

    def wrap_by_word(s, n):
        a = s.split()
        ret = ''
        for i in range(0, len(a), n):
            ret += ' '.join(a[i:i+n]) + '\n'

        return ret

    def launch_url():
        url = str(NSBrowserURLQuery.get())
        if 'https://' in url or '.com' in url:
            webview.create_window(title='', url=url, confirm_close=False, text_select=True, width=800, height=620, frameless=True)
            webview.start()
        elif url == '网址: ' or url == 'URL: ':
            pass
        else:
            if NSBrowserSearchEngine.get() == 0:
                fil = 'https://www.google.com/search?q={}'.format(url)
                webview.create_window(title='', url=fil, confirm_close=False, text_select=True, width=800, height=620, frameless=True)
                webview.start()
            else:
                fil = 'https://www.baidu.com/s?wd={}'.format(url)
                webview.create_window(title='', url=fil, confirm_close=False, text_select=True, width=800, height=620, frameless=True)
                webview.start()

    def launch_url_key(event):
        url = str(NSBrowserURLQuery.get())
        if 'https://' in url or '.com' in url:
            webview.create_window(title='', url=url, confirm_close=False, text_select=True, x=60, y=30, width=800, height=620, frameless=True)
            webview.start()
        elif url == '网址: ' or url == 'URL: ':
            pass
        else:
            if NSBrowserSearchEngine.get() == 0:
                fil = 'https://www.google.com/search?q={}'.format(url)
                webview.create_window(title='', url=fil, confirm_close=False, text_select=True, width=800, height=620, frameless=True)
                webview.start()
            else:
                fil = 'https://www.baidu.com/s?wd={}'.format(url)
                webview.create_window(title='', url=fil, confirm_close=False, text_select=True, width=800, height=620, frameless=True)
                webview.start()

    def change_mode():
        if NSDarkModeStat.get() == 1:
            NSBrowserView.config(bg=dark_theme['bg'])
            NSBrowserIconLabel['bg'] = dark_theme['bg']
            NSBrowserIconLabel['fg'] = dark_theme['fg']
            NSBrowserURLQuery['bg'] = dark_theme['bg']
            NSBrowserURLQuery['fg'] = dark_theme['fg']
            NSBrowserURLQuery['highlightbackground'] = dark_theme['bg']
            NSBrowserURLQuery['highlightcolor'] = dark_theme['fg']
            NSBrowserURLLaunch['bg'] = dark_theme['bg']
            NSBrowserURLLaunch['fg'] = dark_theme['fg']
            NSBrowserURLLaunch.config(activebackground='white', activeforeground='black')

            NSBrowserFavoriteGoogle['bg'] = dark_theme['bg']
            NSBrowserFavoriteGoogle['fg'] = dark_theme['fg']
            NSBrowserFavoriteGoogle.config(activebackground='white', activeforeground='black')
            NSBrowserFavoriteBaidu['bg'] = dark_theme['bg']
            NSBrowserFavoriteBaidu['fg'] = dark_theme['fg']
            NSBrowserFavoriteBaidu.config(activebackground='white', activeforeground='black')
            pass
        else:
            NSBrowserView.config(bg=theme['bg'])
            NSBrowserIconLabel['bg'] = theme['bg']
            NSBrowserIconLabel['fg'] = theme['fg']
            NSBrowserURLQuery['bg'] = theme['bg']
            NSBrowserURLQuery['fg'] = theme['fg']
            NSBrowserURLQuery['highlightbackground'] = theme['bg']
            NSBrowserURLQuery['highlightcolor'] = theme['fg']
            NSBrowserURLLaunch['bg'] = theme['bg']
            NSBrowserURLLaunch['fg'] = theme['fg']
            NSBrowserURLLaunch.config(activebackground='black', activeforeground='white')

            NSBrowserFavoriteGoogle['bg'] = theme['bg']
            NSBrowserFavoriteGoogle['fg'] = theme['fg']
            NSBrowserFavoriteGoogle.config(activebackground='black', activeforeground='white')
            NSBrowserFavoriteBaidu['bg'] = theme['bg']
            NSBrowserFavoriteBaidu['fg'] = theme['fg']
            NSBrowserFavoriteBaidu.config(activebackground='black', activeforeground='white')
            pass

        NSBrowserView.after(ms=500, func=change_mode)

    def change_language():
        if NSLanguageValue.get() == 'en':
            NSBrowserIconLabel['text'] = 'Browser'
            NSBrowserFavoriteGoogle['text'] = 'Google'
            NSBrowserFavoriteBaidu['text'] = 'Baidu'
            pass
        else:
            NSBrowserIconLabel['text'] = '浏览器'
            NSBrowserFavoriteBaidu['text'] = '百度'
            NSBrowserFavoriteGoogle['text'] = '谷歌'
            pass

        NSBrowserView.after(ms=1000, func=change_language)

    def open_baidu():
        webview.create_window(title='', url='https://www.baidu.com', confirm_close=False, text_select=True, width=800, height=620, frameless=True)
        webview.start()
    
    def open_google():
        webview.create_window(title='', url='https://www.google.com', confirm_close=False, text_select=True, width=800, height=620, frameless=True)
        webview.start()

    NSBrowserIconLabel = Label(NSBrowserView, text='浏览器', font=("Futura", 25))
    NSBrowserIconLabel.place(relx=0.5, rely=0.5, anchor=CENTER)

    NSBrowserURLQuery = Entry(NSBrowserView, width=33)
    NSBrowserURLQuery.place(relx=0.41, rely=0.045, anchor=CENTER)
    NSBrowserURLQuery.bind('<FocusIn>', on)
    if NSLanguageValue.get() == 'en':
        NSBrowserURLQuery.insert(0, 'URL: ')
    else:
        NSBrowserURLQuery.insert(0, '网址: ')

    NSBrowserURLLaunch = tkmacosx.Button(NSBrowserView, text='→', width=70, font=("Futura", 14), borderless=1, activeforeground='white', activebackground='black', command=launch_url)
    NSBrowserURLLaunch.place(relx=0.9, rely=0.045, anchor=CENTER)

    NSBrowserFavoriteGoogle = tkmacosx.Button(NSBrowserView, text='谷歌', width=100, height=100, borderless=1, bg='black', fg='white', activebackground='white', activeforeground='black', command=open_google)
    NSBrowserFavoriteGoogle.place(relx=0.3, rely=0.7, anchor=CENTER)

    NSBrowserFavoriteBaidu = tkmacosx.Button(NSBrowserView, text='百度', width=100, height=100, borderless=1, bg='black', fg='white', activebackground='white', activeforeground='black', command=open_baidu)
    NSBrowserFavoriteBaidu.place(relx=0.7, rely=0.7, anchor=CENTER)

    change_mode()
    change_language()
    NSBrowserURLQuery.bind('<Return>', launch_url_key)

def close_experimental_alert():
    NSExperimentalAlert.destroy()
    NSCanvas['bg'] = 'white'
    NSMenuBar.place(relx=0.5, rely=0.012, anchor=CENTER)
    NSWallpaper.place(x=0, y=0, relheight=1, relwidth=1)
    add_apps()
    check_update()

def shutdown(event):
    NSCanvas.destroy()
    root.destroy()

def wallpaper():
    def close_popup():
        NSPopupAlert.destroy()

    NSPopupAlert = Frame(NSControlMenu, width=400, height=420)
    NSPopupAlert.place(relx=0.5, rely=0.7, anchor=CENTER)

    NSPopupTitle = Label(NSPopupAlert, text='选择壁纸: ', fg='#949494', font=("Futura", 20))
    NSPopupTitle.place(relx=0.17, rely=0.05, anchor=CENTER)

    def change_language():
        if NSLanguageValue.get() == 'en':
            NSPopupTitle['text'] = 'Select:'
            NSPopupAlertClose['text'] = 'Close'
            with open(os.getcwd() + '/wallpaper.txt', 'r') as file:
                if file.read() == 'true':
                    NSSetupAutoSwitchWallpaper['text'] = '✓'
                else:
                    NSSetupAutoSwitchWallpaper['text'] = 'Auto'
                    pass
            pass
        else:
            NSPopupTitle['text'] = '选择壁纸: '
            NSPopupAlertClose['text'] = '关闭'
            with open(os.getcwd() + '/wallpaper.txt', 'r') as file:
                if file.read() == 'true':
                    NSSetupAutoSwitchWallpaper['text'] = '✓'
                else:
                    NSSetupAutoSwitchWallpaper['text'] = '自动调整'
                    pass
            pass

        NSPopupAlert.after(ms=1000, func=change_language)

    def auto():
        global NSAutoSwitchCounter
        NSAutoSwitchCounter += 1

        if NSAutoSwitchCounter % 2 == 0:
            NSSetupAutoSwitchWallpaper['text'] = '✓'
            with open(os.getcwd() + '/wallpaper.txt', 'w') as file:
                file.truncate(0)
                file.write('true')
                pass
            pass
        else:
            NSSetupAutoSwitchWallpaper['text'] = '自动调整'
            with open(os.getcwd() + '/wallpaper.txt', 'w') as file:
                file.truncate(0)
                file.write('false')
                pass
            pass

    def w1(event):
        img = Image.open(os.getcwd() + '/wallpaper/1.jpg')
        shutil.copy(src=os.getcwd() + '/wallpaper/1.jpg', dst=os.getcwd() + '/wallpaper.jpg')
        pic = ImageTk.PhotoImage(img)
        NSWallpaper.config(image = pic)
        NSWallpaper.image = pic
    def w2(event):
        img = Image.open(os.getcwd() + '/wallpaper/2.jpg')
        shutil.copy(src=os.getcwd() + '/wallpaper/2.jpg', dst=os.getcwd() + '/wallpaper.jpg')
        pic = ImageTk.PhotoImage(img)
        NSWallpaper.config(image = pic)
        NSWallpaper.image = pic
    def w3(event):
        img = Image.open(os.getcwd() + '/wallpaper/3.jpg')
        shutil.copy(src=os.getcwd() + '/wallpaper/3.jpg', dst=os.getcwd() + '/wallpaper.jpg')
        pic = ImageTk.PhotoImage(img)
        NSWallpaper.config(image = pic)
        NSWallpaper.image = pic
    def w4(event):
        img = Image.open(os.getcwd() + '/wallpaper/4.jpg')
        shutil.copy(src=os.getcwd() + '/wallpaper/4.jpg', dst=os.getcwd() + '/wallpaper.jpg')
        pic = ImageTk.PhotoImage(img)
        NSWallpaper.config(image = pic)
        NSWallpaper.image = pic
    def w5(event):
        img = Image.open(os.getcwd() + '/wallpaper/5.jpg')
        shutil.copy(src=os.getcwd() + '/wallpaper/5.jpg', dst=os.getcwd() + '/wallpaper.jpg')
        pic = ImageTk.PhotoImage(img)
        NSWallpaper.config(image = pic)
        NSWallpaper.image = pic
    def w6(event):
        img = Image.open(os.getcwd() + '/wallpaper/6.jpg')
        shutil.copy(src=os.getcwd() + '/wallpaper/6.jpg', dst=os.getcwd() + '/wallpaper.jpg')
        pic = ImageTk.PhotoImage(img)
        NSWallpaper.config(image = pic)
        NSWallpaper.image = pic
    def w7(event):
        img = Image.open(os.getcwd() + '/wallpaper/7.jpg')
        shutil.copy(src=os.getcwd() + '/wallpaper/7.jpg', dst=os.getcwd() + '/wallpaper.jpg')
        pic = ImageTk.PhotoImage(img)
        NSWallpaper.config(image = pic)
        NSWallpaper.image = pic
    def w8(event):
        img = Image.open(os.getcwd() + '/wallpaper/8.jpg')
        shutil.copy(src=os.getcwd() + '/wallpaper/8.jpg', dst=os.getcwd() + '/wallpaper.jpg')
        pic = ImageTk.PhotoImage(img)
        NSWallpaper.config(image = pic)
        NSWallpaper.image = pic
    def w9(event):
        img = Image.open(os.getcwd() + '/wallpaper/9.jpg')
        shutil.copy(src=os.getcwd() + '/wallpaper/9.jpg', dst=os.getcwd() + '/wallpaper.jpg')
        pic = ImageTk.PhotoImage(img)
        NSWallpaper.config(image = pic)
        NSWallpaper.image = pic
    def w10(event):
        img = Image.open(os.getcwd() + '/wallpaper/10.jpg')
        shutil.copy(src=os.getcwd() + '/wallpaper/10.jpg', dst=os.getcwd() + '/wallpaper.jpg')
        pic = ImageTk.PhotoImage(img)
        NSWallpaper.config(image = pic)
        NSWallpaper.image = pic

    wall1img = Image.open(os.getcwd() + '/wallpaper/1.jpg')
    wall2img = Image.open(os.getcwd() + '/wallpaper/2.jpg')
    wall3img = Image.open(os.getcwd() + '/wallpaper/3.jpg')
    wall4img = Image.open(os.getcwd() + '/wallpaper/4.jpg')
    wall5img = Image.open(os.getcwd() + '/wallpaper/5.jpg')
    wall6img = Image.open(os.getcwd() + '/wallpaper/6.jpg')
    wall7img = Image.open(os.getcwd() + '/wallpaper/7.jpg')
    wall8img = Image.open(os.getcwd() + '/wallpaper/8.jpg')
    wall9img = Image.open(os.getcwd() + '/wallpaper/9.jpg')
    wall10img = Image.open(os.getcwd() + '/wallpaper/10.jpg')
    wall1img = wall1img.resize((40, 70), Image.ANTIALIAS)
    wall2img = wall2img.resize((40, 70), Image.ANTIALIAS)
    wall3img = wall3img.resize((40, 70), Image.ANTIALIAS)
    wall4img = wall4img.resize((40, 70), Image.ANTIALIAS)
    wall5img = wall5img.resize((40, 70), Image.ANTIALIAS)
    wall6img = wall6img.resize((40, 70), Image.ANTIALIAS)
    wall7img = wall7img.resize((40, 70), Image.ANTIALIAS)
    wall8img = wall8img.resize((40, 70), Image.ANTIALIAS)
    wall9img = wall9img.resize((40, 70), Image.ANTIALIAS)
    wall10img = wall10img.resize((40, 70), Image.ANTIALIAS)
    wall1pic = ImageTk.PhotoImage(wall1img)
    wall2pic = ImageTk.PhotoImage(wall2img)
    wall3pic = ImageTk.PhotoImage(wall3img)
    wall4pic = ImageTk.PhotoImage(wall4img)
    wall5pic = ImageTk.PhotoImage(wall5img)
    wall6pic = ImageTk.PhotoImage(wall6img)
    wall7pic = ImageTk.PhotoImage(wall7img)
    wall8pic = ImageTk.PhotoImage(wall8img)
    wall9pic = ImageTk.PhotoImage(wall9img)
    wall10pic = ImageTk.PhotoImage(wall10img)
    wall1 = Label(NSPopupAlert, text='', image=wall1pic)
    wall2 = Label(NSPopupAlert, text='', image=wall2pic)
    wall3 = Label(NSPopupAlert, text='', image=wall3pic)
    wall4 = Label(NSPopupAlert, text='', image=wall4pic)
    wall5 = Label(NSPopupAlert, text='', image=wall5pic)
    wall6 = Label(NSPopupAlert, text='', image=wall6pic)
    wall7 = Label(NSPopupAlert, text='', image=wall7pic)
    wall8 = Label(NSPopupAlert, text='', image=wall8pic)
    wall9 = Label(NSPopupAlert, text='', image=wall9pic)
    wall10 = Label(NSPopupAlert, text='', image=wall10pic)
    wall1.image = wall1pic
    wall2.image = wall2pic
    wall3.image = wall3pic
    wall4.image = wall4pic
    wall5.image = wall5pic
    wall6.image = wall6pic
    wall7.image = wall7pic
    wall8.image = wall8pic
    wall9.image = wall9pic
    wall10.image = wall10pic
    wall1.place(relx=0.15, rely=0.25, anchor=CENTER)
    wall2.place(relx=0.3, rely=0.25, anchor=CENTER)
    wall3.place(relx=0.45, rely=0.25, anchor=CENTER)
    wall4.place(relx=0.6, rely=0.25, anchor=CENTER)
    wall5.place(relx=0.75, rely=0.25, anchor=CENTER)
    wall6.place(relx=0.9, rely=0.25, anchor=CENTER)
    wall7.place(relx=0.15, rely=0.5, anchor=CENTER)
    wall8.place(relx=0.3, rely=0.5, anchor=CENTER)
    wall9.place(relx=0.45, rely=0.5, anchor=CENTER)
    wall10.place(relx=0.6, rely=0.5, anchor=CENTER)
    wall1.bind('<Button-1>', w1)
    wall2.bind('<Button-1>', w2)
    wall3.bind('<Button-1>', w3)
    wall4.bind('<Button-1>', w4)
    wall5.bind('<Button-1>', w5)
    wall6.bind('<Button-1>', w6)
    wall7.bind('<Button-1>', w7)
    wall8.bind('<Button-1>', w8)
    wall9.bind('<Button-1>', w9)
    wall10.bind('<Button-1>', w10)

    NSSetupAutoSwitchWallpaper = tkmacosx.Button(NSPopupAlert, text='自动调整', bg='white', fg='black', font=("Futura", 12), borderless=1, activebackground='white', activeforeground='black', width=75, height=65, command=auto)
    NSSetupAutoSwitchWallpaper.place(relx=0.8, rely=0.49, anchor=CENTER)

    NSPopupAlertClose = tkmacosx.Button(NSPopupAlert, text='关闭', bg='white', fg='black', font=("Futura", 15), borderless=1, activebackground='white', activeforeground='black', command=close_popup)
    NSPopupAlertClose.place(relx=0.5, rely=0.65, anchor=CENTER)

    change_language()

def takedown_pulldown_menu(event):
    try:
        NSWifiControl.place_forget()
        NSWifiLabel.place_forget()
        NSBluetoothControl.place_forget()
        NSBluetoothLabel.place_forget()
        NSShutdownControl.place_forget()
        NSShutdownLabel.place_forget()
        NSWallpaperControl.place_forget()
        NSWallpaperLabel.place_forget()
        NSControlMenu.place_forget()
        NSScreenshotControl.place_forget()
        NSScreenshotLabel.place_forget()
    except:
        pass

def screenshot_takedown_pulldown_menu():
    try:
        NSWifiControl.place_forget()
        NSWifiLabel.place_forget()
        NSBluetoothControl.place_forget()
        NSBluetoothLabel.place_forget()
        NSShutdownControl.place_forget()
        NSShutdownLabel.place_forget()
        NSWallpaperControl.place_forget()
        NSWallpaperLabel.place_forget()
        NSControlMenu.place_forget()
        NSScreenshotControl.place_forget()
        NSScreenshotLabel.place_forget()
    except:
        pass

def clock(event):
    global NSClockView
    NSClockView = Frame(NSWallpaper)
    NSClockView.pack(fill=BOTH, expand=True)
    NSClockView.bind('<Button-1>', takedown_pulldown_menu)

    remove_apps()
    def update_vancouver():
        orig = str(datetime.now())
        fil = orig[11:19]
        NSClockVancouverTime['text'] = fil

        NSClockView.after(ms=1000, func=update_vancouver)

    def update_beijing():
        utc = arrow.utcnow()
        china = utc.to('Asia/Shanghai')
        fil = china.format('HH:mm:ss')
        NSClockBeijingTime['text'] = fil

        NSClockView.after(ms=1000, func=update_beijing)

    def change_mode():
        if NSDarkModeStat.get() == 1:
            NSClockView.config(bg=dark_theme['bg'])
            NSClockVancouver['bg'] = dark_theme['bg']
            NSClockVancouver['fg'] = dark_theme['fg']
            NSClockVancouverTime['bg'] = dark_theme['bg']
            NSClockVancouverTime['fg'] = dark_theme['fg']
            NSClockBeijing['bg'] = dark_theme['bg']
            NSClockBeijing['fg'] = dark_theme['fg']
            NSClockBeijingTime['bg'] = dark_theme['bg']
            NSClockBeijingTime['fg'] = dark_theme['fg']
            pass
        else:
            NSClockView.config(bg='white')
            NSClockVancouver['bg'] = theme['bg']
            NSClockVancouver['fg'] = theme['fg']
            NSClockVancouverTime['bg'] = theme['bg']
            NSClockVancouverTime['fg'] = theme['fg']
            NSClockBeijing['bg'] = theme['bg']
            NSClockBeijing['fg'] = theme['fg']
            NSClockBeijingTime['bg'] = theme['bg']
            NSClockBeijingTime['fg'] = theme['fg']
            pass

        NSClockView.after(ms=500, func=change_mode)

    def change_language():
        if NSLanguageValue.get() == 'en':
            NSClockVancouver['text'] = 'Vancouver'
            NSClockBeijing['text'] = 'Beijing'
            pass
        else:
            NSClockVancouver['text'] = '温哥华'
            NSClockBeijing['text'] = '北京'
            pass

        NSClockView.after(ms=1000, func=change_language)

    NSClockVancouver = Label(NSClockView, text='Vancouver', bg=NSClockView['bg'], font=("Futura", 20), height=4, width=20)
    NSClockVancouver.place(relx=0.19, rely=0.1, anchor=CENTER)

    NSClockVancouverTime = Label(NSClockView, text='', bg=NSClockView['bg'], font=("Futura", 18))
    NSClockVancouverTime.place(relx=0.85, rely=0.1, anchor=CENTER)

    NSClockBeijing = Label(NSClockView, text='北京', bg=NSClockView['bg'], font=("Futura", 20), height=4, width=20)
    NSClockBeijing.place(relx=0.17, rely=0.2, anchor=CENTER)

    NSClockBeijingTime = Label(NSClockView, text='', bg=NSClockView['bg'], font=("Futura", 18))
    NSClockBeijingTime.place(relx=0.85, rely=0.2, anchor=CENTER)

    update_vancouver()
    update_beijing()
    change_mode()
    change_language()

def control_clock():
    def close_popup():
        NSPopupAlert.destroy()

    def update_vancouver():
        orig = str(datetime.now())
        fil = orig[11:19]
        NSClockVancouverTime['text'] = fil

        NSCanvas.after(ms=1000, func=update_vancouver)

    def update_beijing():
        utc = arrow.utcnow()
        china = utc.to('Asia/Shanghai')
        fil = china.format('HH:mm:ss')
        NSClockBeijingTime['text'] = fil

        NSCanvas.after(ms=1000, func=update_beijing)

    def change_mode():
        if NSDarkModeStat.get() == 1:
            NSPopupAlert.config(bg=dark_theme['bg'])
            NSClockVancouver['bg'] = dark_theme['bg']
            NSClockVancouver['fg'] = dark_theme['fg']
            NSClockVancouverTime['bg'] = dark_theme['bg']
            NSClockVancouverTime['fg'] = dark_theme['fg']
            NSClockBeijing['bg'] = dark_theme['bg']
            NSClockBeijing['fg'] = dark_theme['fg']
            NSClockBeijingTime['bg'] = dark_theme['bg']
            NSClockBeijingTime['fg'] = dark_theme['fg']
            pass
        else:
            NSPopupAlert.config(bg=theme['bg'])
            NSClockVancouver['bg'] = theme['bg']
            NSClockVancouver['fg'] = theme['fg']
            NSClockVancouverTime['bg'] = theme['bg']
            NSClockVancouverTime['fg'] = theme['fg']
            NSClockBeijing['bg'] = theme['bg']
            NSClockBeijing['fg'] = theme['fg']
            NSClockBeijingTime['bg'] = theme['bg']
            NSClockBeijingTime['fg'] = theme['fg']
            pass

        NSPopupAlert.after(ms=500, func=change_mode)

    def change_language():
        if NSLanguageValue.get() == 'en':
            NSPopupAlertClose['text'] = 'Close'
            NSClockVancouver['text'] = 'Vancouver'
            NSClockBeijing['text'] = 'Beijing'
            pass
        else:
            NSPopupAlertClose['text'] = '关闭'
            NSClockVancouver['text'] = '温哥华'
            NSClockBeijing['text'] = '北京'
            pass

        NSCanvas.after(ms=1000, func=change_language)

    NSPopupAlert = Frame(NSControlMenu, width=400, height=400)
    NSPopupAlert.place(relx=0.5, rely=0.7, anchor=CENTER)

    NSClockVancouver = Label(NSPopupAlert, text='Vancouver', bg=NSControlMenu['bg'], font=("Futura", 15), height=4, width=20)
    NSClockVancouver.place(relx=0.15, rely=0.2, anchor=CENTER)

    NSClockVancouverTime = Label(NSPopupAlert, text='', bg=NSControlMenu['bg'], font=("Futura", 13))
    NSClockVancouverTime.place(relx=0.8, rely=0.2, anchor=CENTER)

    NSClockBeijing = Label(NSPopupAlert, text='北京', bg=NSControlMenu['bg'], font=("Futura", 15), height=4, width=20)
    NSClockBeijing.place(relx=0.135, rely=0.35, anchor=CENTER)

    NSClockBeijingTime = Label(NSPopupAlert, text='', bg=NSControlMenu['bg'], font=("Futura", 13))
    NSClockBeijingTime.place(relx=0.8, rely=0.35, anchor=CENTER)

    NSPopupAlertClose = tkmacosx.Button(NSPopupAlert, text='关闭', bg='white', fg='black', font=("Futura", 15), borderless=1, activebackground='white', activeforeground='black', command=close_popup)
    NSPopupAlertClose.place(relx=0.5, rely=0.65, anchor=CENTER)

    update_vancouver()
    update_beijing()
    change_mode()
    change_language()

def detect_darkmode():
    response = os.popen('defaults read -g AppleInterfaceStyle').read()
    if 'Dark\n' == response:
        NSDarkModeStat.set(1)
        NSSignalWidget['bg'] = 'white'
        NSBlueSignalWidget['bg'] = 'white'

        NSControlMenu.config(bg=dark_theme['bg'])
        NSBluetoothLabel['bg'] = dark_theme['bg']
        NSBluetoothLabel['fg'] = dark_theme['fg']
        NSWifiLabel['bg'] = dark_theme['bg']
        NSWifiLabel['fg'] = dark_theme['fg']
        NSWallpaperLabel['bg'] = dark_theme['bg']
        NSWallpaperLabel['fg'] = dark_theme['fg']
        NSShutdownLabel['bg'] = dark_theme['bg']
        NSShutdownLabel['fg'] = dark_theme['fg']
        NSClockLabel['bg'] = dark_theme['bg']
        NSClockLabel['fg'] = dark_theme['fg']
        NSScreenshotLabel['bg'] = dark_theme['bg']
        NSScreenshotLabel['fg'] = dark_theme['fg']
        pass
    else:
        NSDarkModeStat.set(0)
        NSSignalWidget['bg'] = 'white'
        NSBlueSignalWidget['bg'] = 'white'

        NSControlMenu.config(bg=theme['bg'])
        NSBluetoothLabel['bg'] = theme['bg']
        NSBluetoothLabel['fg'] = theme['fg']
        NSWifiLabel['bg'] = theme['bg']
        NSWifiLabel['fg'] = theme['fg']
        NSWallpaperLabel['bg'] = theme['bg']
        NSWallpaperLabel['fg'] = theme['fg']
        NSShutdownLabel['bg'] = theme['bg']
        NSShutdownLabel['fg'] = theme['fg']
        NSClockLabel['bg'] = theme['bg']
        NSClockLabel['fg'] = theme['fg']
        NSScreenshotLabel['bg'] = theme['bg']
        NSScreenshotLabel['fg'] = theme['fg']
        pass
    
    root.after(ms=500, func=detect_darkmode)

def change_language():
    if NSLanguageValue.get() == 'en':
        NSPopupTitle['text'] = 'Alert: '
        NSPopupBody['text'] = 'Project-Pios is still developing,\n\nSome Features may not work.'
        NSPopupClose['text'] = 'Dismiss'
        pass
    else:
        NSPopupTitle['text'] = '通知: '
        NSPopupBody['text'] = 'Project-Pios 还在开发中，\n\n部分功能会失效。'
        NSPopupClose['text'] = '好'
        pass

    NSCanvas.after(ms=1000, func=change_language)

def update_languages():
    with open(os.getcwd() + '/language.txt', 'r') as file:
        if file.read() == 'en':
            NSLanguageValue.set('en')
        elif file.read() == 'en\n':
            NSLanguageValue.set('en')
        elif file.read() == 'zh-cn':
            NSLanguageValue.set('zh-cn')
        elif file.read() == 'zh-cn\n':
            NSLanguageValue.set('zh-cn')
        else:
            NSLanguageValue.set('zh-cn')
            pass
    
    NSCanvas.after(ms=1000, func=update_languages)

def screenshot():
    screenshot_takedown_pulldown_menu()
    def wait():
        img = pyscreenshot.grab(bbox=(root.winfo_x(), root.winfo_y(), 400, 800))
        img.show()

        NSCanvas['bg'] = '#4d4d4d'
        NSControlMenu.place(relx=0.5, rely=0.2125, anchor=CENTER)
        NSWifiControl.place(relx=0.1, rely=0.1, anchor=CENTER)
        NSWifiLabel.place(relx=0.1, rely=0.2, anchor=CENTER)
        NSBluetoothControl.place(relx=0.3, rely=0.1, anchor=CENTER)
        NSBluetoothLabel.place(relx=0.3, rely=0.2, anchor=CENTER)
        NSShutdownControl.place(relx=0.5, rely=0.1, anchor=CENTER)
        NSShutdownLabel.place(relx=0.5, rely=0.2, anchor=CENTER)
        NSWallpaperControl.place(relx=0.7, rely=0.1, anchor=CENTER)
        NSWallpaperLabel.place(relx=0.7, rely=0.2, anchor=CENTER)
        NSClockControl.place(relx=0.9, rely=0.1, anchor=CENTER)
        NSClockLabel.place(relx=0.9, rely=0.2, anchor=CENTER)
        NSScreenshotControl.place(relx=0.1, rely=0.4, anchor=CENTER)
        NSScreenshotLabel.place(relx=0.1, rely=0.5, anchor=CENTER)
    
    NSCanvas.after(1000, wait)

def autoswitch_wallpaper():
    with open(os.getcwd() + '/wallpaper.txt', 'r') as file:
        if file.read() == 'true':
            NSAutoSwitchWallpaperStat.set(1)
            if NSDarkModeStat.get() == 1:
                wallimg = Image.open(os.getcwd() + '/wallpaper/9.jpg')
                shutil.copy(src=os.getcwd() + '/wallpaper/9.jpg', dst=os.getcwd() + '/dark_wallpaper.jpg')
                pic = ImageTk.PhotoImage(wallimg)
                NSWallpaper.config(image = pic)
                NSWallpaper.image = pic
            else:
                wallimg = Image.open(os.getcwd() + '/wallpaper/6.jpg')
                shutil.copy(src=os.getcwd() + '/wallpaper/6.jpg', dst=os.getcwd() + '/light_wallpaper.jpg')
                pic = ImageTk.PhotoImage(wallimg)
                NSWallpaper.config(image = pic)
                NSWallpaper.image = pic
        else:
            NSAutoSwitchWallpaperStat.set(0)
            wallimg = Image.open(os.getcwd() + '/wallpaper.jpg')
            pic = ImageTk.PhotoImage(wallimg)
            NSWallpaper.config(image = pic)
            NSWallpaper.image = pic
            pass

    NSCanvas.after(ms=1000, func=autoswitch_wallpaper)

def check_bluetooth():
    with open(os.getcwd() + '/system/bluetooth/bool.txt', 'r') as file:
        if file.read() == 'true':
            os.system('blueutil -p on')
            NSBluetoothControl['bg'] = '#1b73e9'
            NSBluetoothValue.set(1)
            with open(os.getcwd() + '/system/bluetooth/bool.txt', 'w') as file:
                file.truncate(0)
                file.write('true')
                pass
        else:
            os.system('blueutil -p off')
            NSBluetoothControl['bg'] = '#dcdcdc'
            NSBluetoothValue.set(0)
            with open(os.getcwd() + '/system/bluetooth/bool.txt', 'w') as file:
                file.truncate(0)
                file.write('false')
                pass

    NSCanvas.after(ms=1000, func=check_bluetooth)

def check_wifi():
    with open(os.getcwd() + '/system/wifi/bool.txt', 'r') as file:
        if file.read() == 'true':
            os.system('networksetup -setairportpower en0 on')
            NSWifiValue.set(1)
            NSWifiControl['bg'] = '#1b73e9'
            with open(os.getcwd() + '/system/wifi/bool.txt', 'w') as file:
                file.truncate(0)
                file.write('true')
                pass
        else:
            os.system('networksetup -setairportpower en0 off')
            NSWifiValue.set(0)
            NSWifiControl['bg'] = '#dcdcdc'
            with open(os.getcwd() + '/system/wifi/bool.txt', 'w') as file:
                file.truncate(0)
                file.write('false')
                pass
    
    NSCanvas.after(ms=1000, func=check_wifi)

def email(event):
    global NSEmailView
    NSEmailView = Frame(NSWallpaper)
    NSEmailView.pack(fill=BOTH, expand=True)
    NSEmailView.bind('<Button-1>', takedown_pulldown_menu)

    remove_apps()

    def change_language():
        if NSLanguageValue.get() == 'en':
            NSEmailSenderEmailLabel['text'] = 'Receiver:'
            NSEmailSend['text'] = 'Send'
            NSEmailClear['text'] = 'Clear'
            pass
        else:
            NSEmailSenderEmailLabel['text'] = '收件人:'
            NSEmailSend['text'] = '发送'
            NSEmailClear['text'] = '清除'
            pass

        NSEmailView.after(ms=1000, func=change_language)

    def clear():
        NSEmailSenderEmailBox.delete(0, END)
        NSEmailCCBox.delete(0, END)
        NSEmailSubjectBox.delete(0, END)
        NSEmailContent.delete(1.0, END)

        with open(os.getcwd() + '/system/email/email.txt', 'w') as email, open(os.getcwd() + '/system/email/password.txt', 'w') as password:
            email.truncate(0)
            password.truncate(0)

    def send():
        if NSLanguageValue.get() == 'en':
            with open(os.getcwd() + '/system/email/email.txt', 'r') as email, open(os.getcwd() + '/system/email/password.txt', 'r') as password:
                if email.read() == '' or password.read() == '':
                    username = simpledialog.askstring(title='Sign In', prompt='Email')
                    word = simpledialog.askstring(title='Sign In', prompt='Password')
                    pass
                else:
                    username = open(os.getcwd() + '/system/email/email.txt', 'r').read()
                    word = open(os.getcwd() + '/system/email/password.txt', 'r').read()
                    pass
            with yagmail.SMTP(username, word) as yag:
                if NSEmailCCBox.get() == '':
                    yag.send(to=NSEmailSenderEmailBox.get(), subject=NSEmailSubjectBox.get(), contents=NSEmailContent.get(1.0, END))
                    messagebox.showinfo(message=f'Email send to {NSEmailSenderEmailBox.get()}, from {username} was sent.')
                    clear()

                    #write credencials to file for next use
                    with open(os.getcwd() + '/system/email/email.txt', 'w') as email, open(os.getcwd() + '/system/email/password.txt', 'w') as password:
                        email.truncate(0)
                        password.truncate(0)
                        email.write(username)
                        password.write(word)
                        pass
                else:
                    pass
                yag.send(to=NSEmailSenderEmailBox.get(), subject=NSEmailSubjectBox.get(), contents=NSEmailContent.get(1.0, END), cc=NSEmailCCBox.get())
                messagebox.showinfo(message=f'Email send to {NSEmailSenderEmailBox.get()}, from {username} was sent.')
                clear()

                #write credencials to file for next use
                with open(os.getcwd() + '/system/email/email.txt', 'w') as email, open(os.getcwd() + '/system/email/password.txt', 'w') as password:
                    email.truncate(0)
                    password.truncate(0)
                    email.write(username)
                    password.write(word)
                    pass
        else:
            with open(os.getcwd() + '/system/email/email.txt', 'r') as email, open(os.getcwd() + '/system/email/password.txt', 'r') as password:
                if email.read() == '' or password.read() == '':
                    username = simpledialog.askstring(title='登录', prompt='邮箱')
                    word = simpledialog.askstring(title='登录', prompt='密码')
                    pass
                else:
                    username = open(os.getcwd() + '/system/email/email.txt', 'r').read()
                    word = open(os.getcwd() + '/system/email/password.txt', 'r').read()
                    pass
            with yagmail.SMTP(username, word) as yag:
                if NSEmailCCBox.get() == '':
                    yag.send(to=NSEmailSenderEmailBox.get(), subject=NSEmailSubjectBox.get(), contents=NSEmailContent.get(1.0, END))
                    messagebox.showinfo(message=f'从 {username} 的邮件已发送。')
                    clear()

                    #write credencials to file for next use
                    with open(os.getcwd() + '/system/email/email.txt', 'w') as email, open(os.getcwd() + '/system/email/password.txt', 'w') as password:
                        email.truncate(0)
                        password.truncate(0)
                        email.write(username)
                        password.write(word)
                        pass
                else:
                    pass
                yag.send(to=NSEmailSenderEmailBox.get(), subject=NSEmailSubjectBox.get(), contents=NSEmailContent.get(1.0, END), cc=NSEmailCCBox.get())
                messagebox.showinfo(message=f'从 {username} 的邮件已发送。')
                clear()

                #write credencials to file for next use
                with open(os.getcwd() + '/system/email/email.txt', 'w') as email, open(os.getcwd() + '/system/email/password.txt', 'w') as password:
                    email.truncate(0)
                    password.truncate(0)
                    email.write(username)
                    password.write(word)
                    pass

    NSEmailSenderEmailLabel = Label(NSEmailView, text='收件人:', font=("Futura", 15))
    NSEmailSenderEmailLabel.place(relx=0.1, rely=0.048, anchor=CENTER)
    NSEmailSenderEmailBox = Entry(NSEmailView, width=33)
    NSEmailSenderEmailBox.place(relx=0.6, rely=0.045, anchor=CENTER)

    NSEmailCCLabel = Label(NSEmailView, text='CC:', font=("Futura", 15))
    NSEmailCCLabel.place(relx=0.1, rely=0.093, anchor=CENTER)
    NSEmailCCBox = Entry(NSEmailView, width=33)
    NSEmailCCBox.place(relx=0.6, rely=0.093, anchor=CENTER)

    NSEmailSubjectLabel = Label(NSEmailView, text='Subject:', font=("Futura", 15))
    NSEmailSubjectLabel.place(relx=0.1, rely=0.138, anchor=CENTER)
    NSEmailSubjectBox = Entry(NSEmailView, width=33)
    NSEmailSubjectBox.place(relx=0.6, rely=0.138, anchor=CENTER)

    NSEmailSendDivider = ttk.Separator(NSEmailView)
    NSEmailSendDivider.place(relx=0.05, rely=0.17, relwidth=0.9)

    NSEmailContent = Text(NSEmailView, width=56, height=43, font=("Arial", 12))
    NSEmailContent.place(relx=0.5, rely=0.56, anchor=CENTER)

    NSEmailSend = tkmacosx.Button(NSEmailView, text='发送', borderless=1, bg='white', fg='black', activebackground='black', activeforeground='white', width=60, command=send)
    NSEmailSend.place(relx=0.9, rely=0.97, anchor=CENTER)

    NSEmailClear = tkmacosx.Button(NSEmailView, text='清除', borderless=1, bg='white', fg='black', activebackground='black', activeforeground='white', width=60, command=clear)
    NSEmailClear.place(relx=0.1, rely=0.97, anchor=CENTER)

    change_language()

def check_update():
    global NSUpdateAlert
    url = 'https://raw.githubusercontent.com/AccessRetrieved/project-pios/main/version.txt'
    response_version = requests.get(url).content
    version = response_version.decode('utf-8').replace('\n', '')
    NSVersion = StringVar()
    NSVersion.set(version)
    NSUpdateAlert += 1

    if NSUpdateAlert == 1:
        if NSLocalVersion.get() != NSVersion.get():
            if NSLanguageValue.get() == 'en':
                messagebox.showinfo(message='You have a update available. Please go to settings and click on profile. Follow instructions on github to update. \n\n Your version: {v1} \n Target version: {v2}'.format(v1 = NSLocalVersion.get(), v2 = NSVersion.get()))
            else:
                messagebox.showinfo(message='Project-Pios可以更新。请前往设置并单击用户，根据指示更新Project-Pios。\n\n 您的版本: {v1} \n 更新版本: {v2}'.format(v1 = NSLocalVersion.get(), v2 = NSVersion.get()))
        else:
            pass
    else:
        pass

    NSCanvas.after(ms=5000, func=check_update)

def remove_apps():
    APPSettings.place_forget()
    APPBrowser.place_forget()
    APPClock.place_forget()
    APPEmail.place_forget()
    APPAdd.place_forget()
    APPAdd2.place_forget()

def add_apps():
    APPSettings.place(relx=0.2, rely=0.85, anchor=CENTER)
    APPBrowser.place(relx=0.5, rely=0.85, anchor=CENTER)
    APPClock.place(relx=0.8, rely=0.85, anchor=CENTER)
    APPEmail.place(relx=0.2, rely=0.75, anchor=CENTER)
    APPAdd.place(relx=0.5, rely=0.75, anchor=CENTER)
    APPAdd2.place(relx=0.8, rely=0.75, anchor=CENTER)

def destroy_apps():
    try:
        global NSSettingsView
        NSSettingsView.destroy()
    except:
        pass
    try:
        global NSBrowserView
        NSBrowserView.destroy()
    except:
        pass
    try:
        NSClockView.destroy()
    except:
        pass
    try:
        NSEmailView.destroy()
    except:
        pass
    try:
        global NSAppView
        NSAppView.destroy()
    except:
        pass
    try:
        global NSApp2View
        NSApp2View.destroy()
    except:
        pass

def add_app(event): # Manage custom app here
    remove_apps()
    import_app(NSWallpaper)

def add_app2(event): # Manage second custom app here
    remove_apps()
    import_app2(NSWallpaper)

NSCanvas = Canvas(root)
NSCanvas.pack(fill=BOTH, expand=True)

wallpic = Image.open(os.getcwd() + '/wallpaper.jpg')
pic = ImageTk.PhotoImage(wallpic)

NSWallpaper = Label(NSCanvas, text='', image=pic)
NSWallpaper.image = pic
NSWallpaper.place(x=0, y=0, relheight=1, relwidth=1)
NSWallpaper.bind('<Button-1>', takedown_pulldown_menu)

NSMenuBar = Frame(root, height=20, width=400)
NSMenuBar.place(relx=0.5, rely=0.012, anchor=CENTER)
NSMenuBar.bind('<Button-1>', pulldown_menu)

NSDisplayTime = Label(NSMenuBar, text='', bg=NSMenuBar['bg'], font=("Futura", 12))
NSDisplayTime.place(relx=0.5, rely=0.5, anchor=CENTER)
NSDisplayTime.bind('<Button-1>', pulldown_menu)

NSDisplayDate = Label(NSMenuBar, text='', bg=NSMenuBar['bg'], font=("Futura", 12))
NSDisplayDate.place(relx=0.9, rely=0.5, anchor=CENTER)
NSDisplayDate.bind('<Button-1>', pulldown_menu)

NSSignalWidget = Label(NSMenuBar, text='', bg=NSMenuBar['bg'])
NSSignalWidget.place(relx=0.05, rely=0.5, anchor=CENTER)

NSBlueSignalWidget = Label(NSMenuBar, text='', bg=NSMenuBar['bg'])
NSBlueSignalWidget.place(relx=0.1, rely=0.5, anchor=CENTER)

img = Image.open(os.getcwd() + '/wifi.png')
img = img.resize((25, 25), Image.ANTIALIAS)
pic = ImageTk.PhotoImage(img)

NSControlMenu = Frame(NSCanvas, height=300, width=400, bg='white')

NSWifiControl = tkmacosx.CircleButton(NSControlMenu, image=pic, borderless=1, radius=20, command=manage_wifi)
NSWifiLabel = Label(NSControlMenu, text='网络', bg=NSControlMenu['bg'])

blueimg = Image.open(os.getcwd() + '/bluetooth.png')
blueimg = blueimg.resize((20, 20), Image.ANTIALIAS)
bluepic = ImageTk.PhotoImage(blueimg)

NSBluetoothControl = tkmacosx.CircleButton(NSControlMenu, image=bluepic, borderless=1, radius=20, command=manage_bluetooth)
NSBluetoothLabel = Label(NSControlMenu, text='蓝牙', bg=NSControlMenu['bg'])

shutimg = Image.open(os.getcwd() + '/shutdown.png')
shutimg = shutimg.resize((25, 25), Image.ANTIALIAS)
shutpic = ImageTk.PhotoImage(shutimg)

NSShutdownControl = tkmacosx.CircleButton(NSControlMenu, image=shutpic, borderless=1, radius=20)
NSShutdownLabel = Label(NSControlMenu, text='关机', bg=NSControlMenu['bg'])
NSShutdownControl.bind('<Double-1>', shutdown)

wallimg = Image.open(os.getcwd() + '/wallpaper_icon.png')
wallimg = wallimg.resize((25, 25), Image.ANTIALIAS)
wallpic = ImageTk.PhotoImage(wallimg)

NSWallpaperControl = tkmacosx.CircleButton(NSControlMenu, image=wallpic, borderless=1, radius=20, command=wallpaper)
NSWallpaperLabel = Label(NSControlMenu, text='壁纸', bg=NSControlMenu['bg'])

clockimg = Image.open(os.getcwd() + '/clock.png')
clockimg = clockimg.resize((25, 25), Image.ANTIALIAS)
clockpic = ImageTk.PhotoImage(clockimg)

NSClockControl = tkmacosx.CircleButton(NSControlMenu, image=clockpic, borderless=1, radius=20, command=control_clock)
NSClockLabel = Label(NSControlMenu, text='时间', bg=NSControlMenu['bg'])

shotimg = Image.open(os.getcwd() + '/screenshot.png')
shotimg = shotimg.resize((25, 25), Image.ANTIALIAS)
shotpic = ImageTk.PhotoImage(shotimg)

NSScreenshotControl = tkmacosx.CircleButton(NSControlMenu, image=shotpic, borderless=1, radius=20, command=screenshot)
NSScreenshotLabel = Label(NSControlMenu, text='截屏', bg=NSControlMenu['bg'])

NSHomeView = Label(NSCanvas, text=' ', font=("Futura", 1), height=0, width=200, bg='#dddddd')
NSHomeView.place(relx=0.5, rely=0.97, anchor=CENTER)
NSHomeView.bind('<Button-1>', return_home)

appsettingsimg = Image.open(os.getcwd() + '/settings.png')
appsettingsimg = appsettingsimg.resize((40, 40), Image.ANTIALIAS)
appsettingspic = ImageTk.PhotoImage(appsettingsimg)
APPSettings = Label(NSCanvas, text='', image=appsettingspic, border=0)
APPSettings.place(relx=0.2, rely=0.85, anchor=CENTER)
APPSettings.bind('<Button-1>', settings)

appbrowserimg = Image.open(os.getcwd() + '/browser.png')
appbrowserimg = appbrowserimg.resize((40, 40), Image.ANTIALIAS)
appbrowserpic = ImageTk.PhotoImage(appbrowserimg)
APPBrowser = Label(NSCanvas, text='', image=appbrowserpic, border=0)
APPBrowser.place(relx=0.5, rely=0.85, anchor=CENTER)
APPBrowser.bind('<Button-1>', browser)

appclockimg = Image.open(os.getcwd() + '/clock.png')
appclockimg = appclockimg.resize((40, 40), Image.ANTIALIAS)
appclockpic = ImageTk.PhotoImage(appclockimg)
APPClock = Label(NSCanvas, text='', image=appclockpic, border=0)
APPClock.place(relx=0.8, rely=0.85, anchor=CENTER)
APPClock.bind('<Button-1>', clock)

appemailimg = Image.open(os.getcwd() + '/email.png')
appemailimg = appemailimg.resize((40, 40), Image.ANTIALIAS)
appemailpic = ImageTk.PhotoImage(appemailimg)
APPEmail = Label(NSCanvas, text='', image=appemailpic, border=0)
APPEmail.place(relx=0.2, rely=0.75, anchor=CENTER)
APPEmail.bind('<Button-1>', email)

appaddimg = Image.open(NSCustomAppIcon1)
appaddimg = appaddimg.resize((40, 40), Image.ANTIALIAS)
appaddpic = ImageTk.PhotoImage(appaddimg)
APPAdd = Label(NSCanvas, text='', image=appaddpic, border=0) # Open custom app here
APPAdd.place(relx=0.5, rely=0.75, anchor=CENTER)
APPAdd.bind('<Button-1>', add_app)

appadd2img = Image.open(NSCustomAppIcon2)
appadd2img = appadd2img.resize((40, 40), Image.ANTIALIAS)
appadd2pic = ImageTk.PhotoImage(appadd2img)
APPAdd2 = Label(NSCanvas, text='', image=appadd2pic, border=0)
APPAdd2.place(relx=0.8, rely=0.75, anchor=CENTER)
APPAdd2.bind('<Button-1>', add_app2)

NSWallpaper.place_forget()
remove_apps()
NSMenuBar.place_forget()
NSCanvas['bg'] = '#b3b3b3'

NSExperimentalAlert = Frame(NSCanvas, width=380, height=300)
NSExperimentalAlert.place(relx=0.5, rely=0.4, anchor=CENTER)

NSPopupTitle = Label(NSExperimentalAlert, text='通知: ', fg='#949494', font=("Futura", 15))
NSPopupTitle.place(relx=0.1, rely=0.05, anchor=CENTER)

NSPopupBody = Label(NSExperimentalAlert, text='Project-Pios 还在开发中，\n\n部分功能会失效。', font=("Futura", 15))
NSPopupBody.place(relx=0.5, rely=0.45, anchor=CENTER)

NSPopupClose = tkmacosx.Button(NSExperimentalAlert, text='好', font=("Futura", 12), borderless=1, activeforeground='black', activebackground='white', command=close_experimental_alert)
NSPopupClose.place(relx=0.87, rely=0.93, anchor=CENTER)

update_time()
update_date()
update_wifi()
update_bluetooth()
detect_darkmode()
change_language()
update_languages()
autoswitch_wallpaper()
check_bluetooth()
check_wifi()
root.mainloop()