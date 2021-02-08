<a name="top"></a>
# Project-pios
安卓和苹果结合的简单操作系统。 [切换到英文介绍](https://github.com/AccessRetrieved/project-pios/blob/main/English_readme.md)

## 目录
1. [版本](#version)
2. [下载和运行](#install)
3. [已知问题](#bugs)
4. [语言](#language)
5. [图片介绍](#images)
6. [帮手](#helpers)
***

### 屏幕过于小的电脑不支持
用PC的暂时不支持

<a name="version"></a>
## 版本
- **版本5.1**
   - 完善了朋友软件， 可在里面查看屏幕使用时间
   - 模拟器设置里的屏幕使用时间表格用tkinter替换了plt.show()
- **版本5.0**
   - 添加了屏幕使用时间和记录
   - 添加了模拟器设置 (可用`Command-,`打开)
- **版本4.0.8**
   - 添加了自动识别相册二维码功能
- **版本4.0.7**
   - 添加了launch文件夹：任何launch文件夹里的文件将在Project-Pios开始时打开
   - 修复了一些bugs
- **版本4.0.6**
   - 修复了一些Bugs
- **版本4.0.5**
   - 添加了睡眠功能
   - 重新规划了文件系统
- **版本4.0.4**
   - 修复了一些Bugs
- **版本4.0.4**
   - 修复了一些Bugs
- **版本4.0.3**
   - 支持两种自创软件
- **版本4.0.2**
   - 修复了自动检查更新功能
   - 调整了浏览器
- **版本4.0.1**
   - 添加了自动查看更新功能
   - 可运行自主软件用：app.py
- **版本4.0**（需要重新运行`pip3 install -r r.txt` 或 `pip install -r r.txt`)
   - 添加了邮件功能
   - 修复了浏览器截屏功能
- **版本3.5.4**
   - 添加了系统控制
- **版本3.5.3**
   - 添加了双击关机功能
- **版本3.5.2**
   - 快捷菜单可在其他应用打开
   - 可在其他应用上截屏
   - 修复了自动切换壁纸的bugs
- **版本3.5.1**
   - 添加了自动切换壁纸功能
   - 修复了一些暗模式的bugs
   - 修复了设置
- **版本3.5**（需要重新运行`pip3 install -r r.txt` 或 `pip install -r r.txt`)
   - 可选择语言：英语和中文
   - 添加了截屏功能
   - 修复了一些bugs
- **版本3.0**（需要重新运行`pip3 install -r r.txt` 或 `pip install -r r.txt`)
   - 添加了暗模式
   - 支持实时切换暗模式（需要macos Big sur - 11.1以上开启手动切换/macos Catalina支持自动切换）
   - 设置里的用户添加了功能
   - 修复了一些bugs
- **版本2.5**（需要重新运行`pip3 install -r r.txt` 或 `pip install -r r.txt`)
   - 添加了”时间“软件
   - 可在快捷菜单里选择时间选项
- **版本1.5** （还在用版本1.0的需要重新运行`pip3 install -r r.txt` 或 `pip instal -r r.txt`)
   - 换了蓝牙模块
   - 可以选择桌面布局和壁纸
   - 添加了浏览器
   - 隐私设置：开/关 摄像头，麦克风，和系统通知
- **版本1.0**
   - 网络
   - 蓝牙
   - 设置

<a name="install"></a>
## 下载和运行
1. [下载](https://www.python.org/ftp/python/3.9.1/python-3.9.1-macosx10.9.pkg) python3.9
2. 打开终端
3. 运行以下载(复制粘贴简单些)：`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
4. 运行：`brew install blueutil`
5. 运行：`cd Desktop`
6. 运行：`git clone https://github.com/AccessRetrieved/Project-Pios`
7. 运行：`cd Project-Pios`
8. 运行： `pip3 install -r r.txt` - 如果出错，运行`pip install -r r.txt`
9. 运行：`mv project_pios ..`
10. 运行：`cd ..`
11. 运行：`rm -rf Project-Pios`
12. 运行： `cd project_pios`
13. 所需的模块都下载完了，现在运行：`python3 main.py` - 如果出错，运行`python main.py`

<a name="bugs"></a>
## 已知问题
1. 切换到暗模式的时候蓝牙模块和wifi模块需要新的图片资源

<a name="language"></a>
## 更改语言
把language.txt的“en“改成”zh-cn“以转换语言。

<a name="images"></a>
## 图片介绍
![1](https://i.ibb.co/gPq0pNW/Screen-Shot-2021-01-23-at-1-10-59-PM.png)
![2](https://i.ibb.co/Lp6j161/Screen-Shot-2021-01-23-at-1-11-25-PM.png)
![3](https://i.ibb.co/FqknCvn/Screen-Shot-2021-01-23-at-1-11-36-PM.png)

<a name="helpers"></a>
## 帮手
1. [图片转文字](https://github.com/AccessRetrieved/OCR/tree/master)
2. [扫描二维码](https://github.com/AccessRetrieved/Qr-Code-Scanner)

[回到顶部 ↑](#top)
