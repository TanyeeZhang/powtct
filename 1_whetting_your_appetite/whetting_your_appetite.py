# coding=utf-8
"""
   Filename: whetting_your_appetite
   Author: Tanyee
   Date: 2020/3/26
   Original: https://docs.python.org/3.7/tutorial/index.html
   Description: Whet your appetite is a phrase meaning to "sharpen one's desire for food" whereas
                the food here means Python.
"""
"""
If you do much work on computers, eventually you find that there’s some task you’d like to automate. For example, 
you may wish to perform a search-and-replace over a large number of text files, or rename and rearrange a bunch of 
photo files in a complicated way. Perhaps you’d like to write a small custom database, or a specialized GUI application, 
or a simple game.

## 如果你经常在电脑上工作，总会有些任务会想让它自动化。比如，对一大堆文本文件进行查找替换，对很多照片文件按照比较复杂的规则重命名并放入不同的文件夹。
也可能你想写一个小型的数据库应用，一个特定的图形界面应用，或者一个简单的游戏。##

[[ 如果你在电脑上做很多工作，最终你会发现有一些任务你想让它完成自动化。举个例子，你可能希望查找在非常多的文本文件里做查找替换，或者用一种复杂的方式
重命名和重排一大堆的照片文件。可能你想写一个小型的定制化数据库，或者特定的图形界面应用程序，或者一个简单的游戏。]]
"""

"""
If you’re a professional software developer, you may have to work with several C/C++/Java libraries but find the usual 
write/compile/test/re-compile cycle is too slow. Perhaps you’re writing a test suite for such a library and find writing 
the testing code a tedious task. Or maybe you’ve written a program that could use an extension language, and you don’t 
want to design and implement a whole new language for your application.

## 如果你是专业的软件开发人员，你可能需要编写一些 C/C++/Java 库，但总觉得通常的 编写、编译、测试、再次编译 流程太慢了。
可能给这样的库写一组测试，就是很麻烦的工作了。或许你写了个软件，可以支持插件扩展语言，但你不想为了自己这一个应用，专门设计
和实现一种新语言了。##

[[ 如果你是一个专业的软件开发者，你也许不得不使用一些C、C++、Java库，但是发现通常的编写、编译、测试、重新编译的周期极其漫长。
可能你为一个库在写一个测试用例，发现写测试代码是一个乏味的任务。或者也许你已经写了一个可以使用一种扩展语言的程序，你不想为你的应用
设计实现一个全新的语言。]]
"""

"""
Python is just the language for you.

## 那么，Python 正好能满足你的需要。##

[[ Python就是为你而生。]]
"""

"""
You could write a Unix shell script or Windows batch files for some of these tasks, but shell scripts are best at 
moving around files and changing text data, not well-suited for GUI applications or games. You could write a C/C++/Java 
program, but it can take a lot of development time to get even a first-draft program. Python is simpler to use, 
available on Windows, Mac OS X, and Unix operating systems, and will help you get the job done more quickly.

## 对于这些任务，你也可以写 Unix shell 脚本或者 Windows 批处理完成，但是 shell 脚本最擅长移动文件和替换文本，并不适合 GUI 界面或者游戏开发。
你可以写一个 C/C++/Java 程序，但是可能初稿都要很长的开发时间。Python 的使用则更加简单，可以在 Windows，Mac OS X，以及 Unix 操作系统上使用，
而且可以帮你更快地完成工作。##

[[ 你可以为某些任务写一个Unix shell脚本或者Windows批处理文件，但shell脚本最擅长于操作文件和改变文件内容，并不很好地适用于图形界面应用或者游戏。
你可以写一个C、C++、Java程序，但是它要花费大量的开发时间，甚至是第一次运行程序。Python用起来更简单，适用于Windows，Mac OS X，Unix操作系统，
它将会帮助你更快地完成工作。]]
"""

"""
Python is simple to use, but it is a real programming language, offering much more structure and support for large 
programs than shell scripts or batch files can offer. On the other hand, Python also offers much more error checking 
than C, and, being a very-high-level language, it has high-level data types built in, such as flexible arrays and 
dictionaries. Because of its more general data types Python is applicable to a much larger problem domain than Awk or 
even Perl, yet many things are at least as easy in Python as in those languages.

## Python 很容易使用，但它是一种真正的编程语言，提供了很多数据结构，也支持大型程序，远超 shell 脚本或批处理文件的功能。Python 还提供比 C 语言
更多的错误检查，而且作为一种 “超高级语言”，它有高级的内置数据类型，比如灵活的数组和字典。正因为这些更加通用的数据类型，Python 能够应付更多的问题，
超过 Awk 甚至 Perl，而且很多东西在 Python 中至少和那些语言同样简单。##

[[ Python虽然用起来简单，但它是一门真正的编程语言，相较shell脚本或者批处理文件，Python为大型的程序提供了更多的结构与支持。另一方面，Python
也比C语言提供了更多的错误检查，而且作为一门高级编程语言，它内置了高级的数据类型，比如灵活的数组和字典。因为Python拥有更多普适性的数据类型，所以
Python适用于比Awk甚至Perl更大的领域，然而Python做很多事情都至少和那些语言一样简单。]]
"""

"""
Python allows you to split your program into modules that can be reused in other Python programs. It comes with a large 
collection of standard modules that you can use as the basis of your programs — or as examples to start learning to 
program in Python. Some of these modules provide things like file I/O, system calls, sockets, and even interfaces to 
graphical user interface toolkits like Tk.

## Python允许你将程序划分为能在其他的Python程序中重复利用的模块。它内置了很多的标准模块，你可以在此基础上开发程序——也可以作为例子，
开始学习Python编程。例如，一切内置模块提供诸如文件输入输出、系统调用、套接字、甚至图形界面接口工作包比如Tk。##

[[ Python允许你将你的程序切割小的模块，可以被别的Python程序复用。有大量的标准库供你使用来作为你程序的基础，或者作为你开始学习Python的例子。
其中一些模块提供像I/O，系统调用等功能，甚至还有图形用户接口工具比如TK。]]
"""

"""
Python is an interpreted language, which can save you considerable time during program development because no 
compilation and linking is necessary. The interpreter can be used interactively, which makes it easy to experiment 
with features of the language, to write throw-away programs, or to test functions during bottom-up program development. 
It is also a handy desk calculator.

## Python是一种解释型语言，在程序开发阶段可以为你节省大量时间，因为不需要编译和链接。解释器可以交互式使用，这样就可以方便地尝试语言特性，
写一些一次性的程序，或者在自底向上的程序开发中测试功能。它也是一个顺手的桌面计算器。##

[[ Python是一门解释性的语言，在开发过程中，它可以为你节省大量的时间，因为无需编译和链接。解释器可以交互使用，因此尝试语言的特性，写一些随手丢弃的程序，
或者在自底向上的开发过程中测试一些方法，都变得很简单。它也是一个手边的桌面计算器。]]

"""

"""
Python enables programs to be written compactly and readably. Programs written in Python are typically much shorter 
than equivalent C, C++, or Java programs, for several reasons:
the high-level data types allow you to express complex operations in a single statement;
statement grouping is done by indentation instead of beginning and ending brackets;
no variable or argument declarations are necessary.

## Python程序的书写是紧凑而易读的。Python代码通常比同样功能的C，C++，Java代码要短很多，有如下几个原因：
高级数据类型允许在一个表达式中表示复杂的操作；
代码块的划分是按照缩进而不是成对的花括号；
不需要预先定义变量或参数。##

[[ Python使程序变得写起来简单读起来好读。具有代表性的就是，同样的C，C++，Java程序，用Python写起来就短好多，有以下几个原因：
高级的数据类型允许你在单个语句中做更复杂的操作；
语句段落靠缩进完成，而不是左右大括号；
没有变量或参数声明也是可以的。]]
"""

"""
Python is extensible: if you know how to program in C it is easy to add a new built-in function or module to the 
interpreter, either to perform critical operations at maximum speed, or to link Python programs to libraries that may 
only be available in binary form (such as a vendor-specific graphics library). Once you are really hooked, 
you can link the Python interpreter into an application written in C and use it as an extension or command language for 
that application.

## Python是“可扩展的”：如果你知道怎么写C语言程序，就能很容易地给解释器添加新的内置函数或模块，不论是让关键的操作以最高速度运行，
还是把Python程序链接到只提供预编译程序的库（比如硬件相关的图形库）。一旦你真正链接上了，就能在Python解释器中扩展或者控制C语言编写的应用了。##

[[ Python是可扩展的：如果你知道如何用C语言编程，那么给解释器添加一个新的内置程序或模块很简单，要么以最大速度执行一个重要的操作，要么链接
Python程序到适用于二进制形式的库上面（比如一个特定供应商的图形库）。一旦你被真正地钩住，你可以链接Python解释器到C应用程序里，然后把它当做
程序的扩展扩展或命令语言。]]
"""

"""
By the way, the language is named after the BBC show “Monty Python’s Flying Circus” and has nothing to do with reptiles. 
Making references to Monty Python skits in documentation is not only allowed, it is encouraged!

## 顺便提一下，这种语言的名字（python 一词直译为 “蟒蛇”）得名自BBC节目“Monty Python的飞行马戏团” ，而与爬行动物没有关系。
在文档中用Monty Python来开玩笑不只是被允许的，还是被推荐的！##

[[ 顺便说一句，这门语言是在BBC播放“Monty Python’s Flying Circus”之后命名的，所以和爬行动物无关。在文档中参考Monty Python小品
不仅是允许的，而且是鼓励的。]]
"""

"""
Now that you are all excited about Python, you’ll want to examine it in some more detail. Since the best way to learn a 
language is to use it, the tutorial invites you to play with the Python interpreter as you read.

## 现在你已经对Python跃跃欲试了，想要深入了解一些细节了。因为学习语言的最佳方式是使用它，本教程邀请你一边阅读，一边在Python解释器中玩耍。##

[[ 现在你在对Python感到很兴奋，你将想从更多的细节去试验它。由于学习一门语言最好的方式就是使用它，因此这个教程邀你在阅读时使用
Python解释器作为实战。]]
"""

"""
In the next chapter, the mechanics of using the interpreter are explained. This is rather mundane information, 
but essential for trying out the examples shown later.

## 在下一章节，会讲解使用解释器的方法。看起来相当枯燥，但是对于尝试后续的例子来说，是非常关键的。##

[[ 在下一章，我们将阐述解释器的原理。内容相当平实，但对试验后面的例子是绝对必要的。]]
"""

"""
The rest of the tutorial introduces various features of the Python language and system through examples, beginning with 
simple expressions, statements and data types, through functions and modules, and finally touching upon advanced 
concepts like exceptions and user-defined classes.

## 教程的其他部分将通过示例介绍 Python 语言和系统中的不同功能，开始是比较简单的表达式、语句和数据类型，然后是函数和模块，最终接触
一些高级概念，比如异常、用户定义的类。##

[[ 教程的其余内容通过例子介绍了Python语言的各种特性，以简单的表达式，语句，数据类型开始，直到方法和模块，最后接触一些高级的概念，
比如异常和用户自定义类。]]
"""

"""
[VOCABULARY]
applicable: 可适用的;可应用的
considerable: 相当大的;重要的
interactive: 交互式的;相互作用的
compact: adj.紧凑的,简洁的;n.小汽车,契约;v.使简洁，使紧密
indent: v.缩排,订货;n.征用令,缩进
critical: 关键的;临界的
suite: 家具;套房
mechanics: 力学;结构;技术
vendor: 卖主;小贩;供应商
tedious: 沉闷的;冗长乏味的
first draft: 初稿
try out: 试验;考验;提炼
name after: 以...命名
mundane: 世俗的;平凡的
touch upon: 涉及;触及
"""