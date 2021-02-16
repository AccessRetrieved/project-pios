from getpass import getuser

"""
Project-Pios设置文件
普通设置可以在模拟器设置里进行(Command+,)

Config file for Project-Pios.

Most settings can be made in simulator settings(Command+,) and Project-Pios settings.
"""

# 窗口大小设置，屏幕小的电脑可以改成300x700
# Window size, macs with a smaller screen can switch to 300x700
window_width = 400
window_height = 800

# 启动时自动打开launch文件夹里里的文件, 改成False以关闭
# Auto launch "launch" folder's content. Change auto_launch to false to omit function
auto_launch = True

'''
用户的名字，getuser()为自动提取用户名
name = '我的名字'

Profile name, change to getuser() for default username
name = 'example name'
'''
name = getuser()

'''
设置中单击用户打开的网页
可以改成自己的网页
profile_url = 'https://google.com'

URL to open when profile inside Project-Pios settings is clicked
Can set to custom url
profile_url = 'https://google.com'
'''

profile_url = 'https://github.com/AccessRetrieved/Project-Pios'