# coding=utf-8
"""
   Filename: 2_1_2_interactive_mode
   Author: Tanyee
   Date: 2020/3/26
   Original: https://docs.python.org/3.7/tutorial/interpreter.html#interactive-mode
   Description: Interactive mode.
"""

"""
When commands are read from a tty, the interpreter is said to be in interactive mode. In this mode it prompts for the 
next command with the primary prompt, usually three greater-than signs (>>>); for continuation lines it prompts with 
the secondary prompt, by default three dots (...). The interpreter prints a welcome message stating its version number 
and a copyright notice before printing the first prompt:

## 在终端（tty）输入并执行指令时，我们说解释器是运行在交互模式（interactive mode）。在这种模式中，它会显示主提示符（primary prompt），
提示输入下一条指令，通常用三个大于号（>>>）表示；连续输入行的时候，它会显示次要提示符，默认是三个点（...）。进入解释器时，它会先显示欢迎信息、
版本信息、版权声明，然后就会出现提示符：##

[[ 当tty设备读到命令，解释器就处于交互模式了。在这个模式下，主提示符通常会用三个大于号（>>>）来提示输入；默认用三个点（...）来提示输入连续的句子。
解释器打印会在第一个提示符之前，输出一个欢迎信息展示它的版本号和版权信息。]]
"""

"""
$ python3.7
Python 3.7 (default, Sep 16 2015, 09:25:04)
[GCC 4.8.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
"""

"""
Continuation lines are needed when entering a multi-line construct. As an example, take a look at this if statement:

## 多行指令需要在连续的多行中输入。比如，以if为例：##

[[ 输入多行语句结构的时候，需要连续的句子。举个例子，请看这个if语句：]]
"""

"""
>>> the_world_is_flat = True
>>> if the_world_is_flat:
...     print("Be careful not to fall off!")
...
Be careful not to fall off!
"""

"""
For more on interactive mode, see Interactive Mode.

## 有关交互模式的更多内容，请见<交互模式>。##

[[ 更多关于交互模式的内容，请看<交互模式>]]
"""

"""
[VOCABULARY]
continuation: 继续;续集;延长
state: v.规定;声明;n.国家;州;情形
fall off: 下降;减少
"""