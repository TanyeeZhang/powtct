# coding=utf-8
"""
   Author: Tanyee
   Date: 2020/3/26
   Original: https://docs.python.org/3.7/tutorial/interpreter.html#
   Description: The Chapter preface.
"""

"""
The Python interpreter is usually installed as /usr/local/bin/python3.7 on those machines where it is available; 
putting /usr/local/bin in your Unix shell’s search path makes it possible to start it by typing the command:
python3.7
to the shell. Since the choice of the directory where the interpreter lives is an installation option, other places are 
possible; check with your local Python guru or system administrator. 
(E.g., /usr/local/python is a popular alternative location.)

## 在Python可用的机器上，Python解释器通常放在/usr/local/bin/python3.7; 把/usr/local/bin 放到你Unix shell的搜索路径当中,这样就能键入命令:
Python3.7
就能运行了。安装时可以选择安装目录，所以解释器也可能在别的地方；可以问问你身边的Python大牛，或者你的系统管理员。（比如 /usr/local/python 也是比较常用的备选路径）##

[[ Python解释器通常安装在/usr/local/bin/python3.7，在你的Unix shell里进入/usr/local/bin路径下，输入Python3.7命令进入shell。由于选择解释器在哪个文件夹
取决于安装选项，所以别的位置也是可能的；检查你本地的Python或者系统管理者。（比如，/usr/local/python是一个受欢迎的可选位置。）]]
"""

"""
On Windows machines where you have installed Python from the Microsoft Store, the python3.7 command will be available. 
If you have the py.exe launcher installed, you can use the py command. See Excursus: Setting environment variables for 
other ways to launch Python.

## 在 Windows 机器上当你从 Microsoft Store 安装 Python 之后，python3.7 命令将可使用。如果你安装了py.exe启动器，你将可以使用py命令。 
参阅<附录：设置环境变量>了解其他启动Python的方式。##

[[ 在Windows机器上从微软商店安装Python，那个python3.7的命令是可以的。如果你是用py.exe下载器安装的，你可以用py命令。
详见附录：其它安装Python方式环境变量的设置。]]
"""

"""
Typing an end-of-file character (Control-D on Unix, Control-Z on Windows) at the primary prompt causes 
the interpreter to exit with a zero exit status. If that doesn’t work, you can exit the interpreter by 
typing the following command: quit().

## 在主提示符中输入文件结束字符（在Unix系统中是Control-D，Windows系统中是Control-Z）就退出解释器并返回退出状态为0。
如果这样不管用，你还可以写这个命令退出：quit()。##

[[ 在输入框内输入一个文件结束字符（在Unix上是Control-D，在Windows上是Control-Z）使解释器以状态码0退出。如果那样不好使，你也可以
输入这样的命令：quit()。]]
"""

"""
The interpreter’s line-editing features include interactive editing, history substitution and code completion 
on systems that support the GNU Readline library. Perhaps the quickest check to see whether command line editing is 
supported is typing Control-P to the first Python prompt you get. If it beeps, you have command line editing; see 
Appendix Interactive Input Editing and History Substitution for an introduction to the keys. If nothing appears 
to happen, or if ^P is echoed, command line editing isn’t available; you’ll only be able to use backspace to remove 
characters from the current line.

## 解释器的行编辑功能在支持 GNU Readline 库的系统中也包括交互式编辑，历史替换和代码补全等。 检测是否支持行编辑最快速的方式是在首次出现Python 
提示符时输入Control-P。如果听到“哔”提示音，就说明支持行编辑；请参阅附录<交互式编辑和编辑历史>了解有关功能键的介绍。如果什么都没发生，或是回显了^P，
说明不支持行编辑；你只能用退格键从当前行中删除字符。##

[[ 解释器的行编辑功能包括交互式的编辑，之前输入的代码不用二次输入和代码补全，这些功能需要系统支持GNU Readline库。可能命令行编辑功能最快的
检查方法就是在你的第一步得到的Python输入框里输入Control-P。如果响了嘟一声，说明你有这个命令行编辑功能；查阅Appendix Interactive Input Editing 
and History Substitution来获取关键内容介绍。如果什么事也没发生，或者返回了^P，那命令行编辑就不可用；你只能用退格键删掉当前这一行了。]]

"""

"""
The interpreter operates somewhat like the Unix shell: when called with standard input connected to a tty device, it 
reads and executes commands interactively; when called with a file name argument or with a file as standard input, 
it reads and executes a script from that file.

## 解释器运行的时候有点像Unix命令行：在一个标准输入tty设备上调用，它能交互式地读取和执行命令；调用时提供文件名参数，或者有个文件重定向到标准
输入的话，它就会读取和执行文件中的脚本。##

[[ 解释器的操作有点儿像Unix shell:当标准输入连接到一个TTY设备（远程终端），交互式地读取和执行命令；当一个文件名参数被调用或者将一个文件当作标准输入，
就将从那个文件读取和执行脚本。]]
"""

"""
A second way of starting the interpreter is python -c command [arg] ..., which executes the statement(s) in command, 
analogous to the shell’s -c option. Since Python statements often contain spaces or other characters that are special 
to the shell, it is usually advised to quote command in its entirety with single quotes.

## 另一种启动解释器的方式是 python -c command [arg] ...，其中command要换成想执行的指令，就像命令行的-c选项。由于Python代码中经常会包含对终端来说
比较特殊的字符，通常情况下都建议用英文单引号把command括起来。##

[[ 启动解释器的第二种方式就是“python -c command [arg] ...”，这个命令可以在命令行里执行语句，和shell的-c选项类似。由于Python语句经常包含空格
或者其它shell中的特殊字符，所以通常建议引用命令时用单引号来复制。]]
"""

"""
Some Python modules are also useful as scripts. These can be invoked using python -m module [arg] ..., which executes 
the source file for module as if you had spelled out its full name on the command line.

## 有些Python模块也可以作为脚本使用。可以这样输入：python -m module [arg] ...，这会执行module的源文件，就跟你在命令行把路径写全了一样。##

[[ 一些Python模块也和脚本一样有用。调用“python -m module [arg] ...”来执行源文件，就好像你已经在命令行里拼出它的全名。]]
"""

"""
When a script file is used, it is sometimes useful to be able to run the script and enter interactive mode afterwards. 
This can be done by passing -i before the script.

## 在运行脚本的时候，有时可能也会需要在运行后进入交互模式。这种时候在文件参数前，加上选项-i就可以了。##

[[ 使用脚本文件时，有时能够运行脚本很有用并且进入交互模式。可以在脚本前面传入-i来实现。]]
"""

"""
All command line options are described in Command line and environment.

## 关于所有的命令行选项，请参考<命令行与环境>。##

[[所有的命令行选项都在命令行与环境中描述了。]]
"""

"""
[VOCABULARY]
alternative: adj.供选择的;n.供替代的选择
excursus: 附录,补说
somewhat: 有点,稍微
analogous: 类似的,模拟的
quote: v.引述,报价;n.引文,引号
"""
