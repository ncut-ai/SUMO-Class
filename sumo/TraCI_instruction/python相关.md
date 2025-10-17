## Python相关

查看python版本,在命令提示符中输入

```dos
​python –V​
python --version
```

使用 python代码查看版本号

```python
import sys
#sys模块提供了一系列有关Python运行环境的变量和函数。
print(sys.version)
#sys.version用来获取Python解释程序的版本信息
```

或者

```python
import platform
#platform模块给我们提供了很多方法去获取操作系统的信息
print(platform.python_version())
#platform.python_version()可以获得计算机中python的版本
```

通过以下命令来判断是否已安装：

```dos
pip --version     # Python2.x 版本命令
pip3 --version    # Python3.x 版本命令
```

显示版本和路径

```dos
pip --version
```

获取帮助

```dos
pip --help
```

升级 pip

```dos
pip install -U pip
```

安装包

```dos
pip install SomePackage              # 最新版本
pip install SomePackage==1.0.4       # 指定版本
pip install 'SomePackage>=1.0.4'     # 最小版本
```

比如我要安装 Django。用以下的一条命令就可以，方便快捷。

```dos
pip install Django==1.7
```

升级包

```dos
pip install --upgrade SomePackage
```

升级指定的包，通过使用==, >=, <=, >, < 来指定一个版本号。

卸载包

```dos
pip uninstall SomePackage
```

搜索包

```dos
pip search SomePackage
```

显示安装包信息

```dos
pip show 
```

查看指定包的详细信息

```dos
pip show -f SomePackage
```

列出已安装的包

```dos
pip list
```

查看可升级的包

```dos
pip list -o
```

Windows 平台升级：

```dos
python -m pip install -U pip   # python2.x
python -m pip3 install -U pip    # python3.x
```

pip 清华大学开源软件镜像站

使用国内镜像速度会快很多：

临时使用：

```dos
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
```

例如，安装 Django：

```dos
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple Django
```

如果要设为默认需要升级 pip 到最新的版本 (>=10.0.0) 后进行配置：

```dos
pip install pip -U
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

如果您到 pip 默认源的网络连接较差，临时使用本镜像站来升级 pip：

```dos
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U
```

## Getting started with VS Code for Python

Make sure that you select the option to Add Python to PATH during installation (via the installer).

### 安装VSCODE

- First, head over to to code.visualstudio.com and grab the installer for your specific platform.
- Once VS Code is installed, head over to the Extensions tab in the sidebar on the left by clicking on it or by pressing CTRL+SHIFT+X. Search for the 'Python' extension published by Microsoft and click on Install.

### Usage and Configuration

- The Python extension in VS Code allows you to directly run a Python file by clicking on the 'Play' button on the top-right corner of the editor (without having to type python file.py in the terminal).
- You can also do it by pressing CTRL+SHIFT+P to open the Command Palette and running the > Python: Run File in Terminal command.
- Finally, you can configure VS Code's settings by going to File > Preferences > Settings or by pressing CTRL+COMMA. In VS Code, each individual setting has an unique identifier which you can see by clicking on the cog wheel that appears to the left of each setting and clicking on 'Copy Setting ID'. This ID is what will be referred to while talking about a specific setting. You can also search for this ID in the search bar under Settings.

### Linting and Formatting Support

- For VS Code to provide linting support for your projects, you must first install a preferred linter like flake8 or pylint.

```python
pip install flake8
```

- To enable linters, open the Command Palette (Ctrl+Shift+P) and select the **Python: Select Linter command**. The Select Linter command adds "python.linting.<linter>Enabled": true to your settings, where <linter> is the name of the chosen linter. See Specific linters for details.

Enabling a linter prompts you to install the required packages in your selected environment for the chosen linter.

- To perform linting, open the Command Palette (Ctrl+Shift+P), filter on "linting", and select Python: Run Linting. Linting will run automatically when you save a file.