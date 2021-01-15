# project-pios
Project-pios(python-os). 安卓和苹果结合的简单操作系统。
窗口大小：400x800

### 暂时只支持Macbook Air 2018+ 或更好的电脑，比如macbook pro(原因？因为老的电脑屏幕太小这软件装不下)
用PC的暂时不支持

## 版本
1. 版本1.0
   - 网络
   - 蓝牙
   - 设置
2. 版本1.5 （还在用版本1.0的需要重新运行`pip3 install -r r.txt` 或 `pip instal -r r.txt`)
   - 换了蓝牙模块
   - 可以选择桌面布局和壁纸
   - 添加了浏览器

## 下载和运行
1. [下载](https://www.python.org/ftp/python/3.9.1/python-3.9.1-macosx10.9.pkg) python3.9
2. 打开终端
3. 运行以下载(复制黏贴不然会出错)：`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
4. 运行：`brew install blueutil`
3. 运行：`git clone https://github.com/AccessRetrieved/project-pios`
4. 运行：`cd project-pios`
5. 运行： `pip3 install -r r.txt` - 如果出错，打`pip install -r r.txt`
6. 运行： `cd project_pios`
7. 所需的模块都下载完了，现在运行：`python3 main.py` - 如果出错，打`python main.py`
