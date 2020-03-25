# coding=utf-8
"""
   Filename: introduction
   Author: Tanyee
   Date: 2020/3/25
   Original: https://docs.python.org/3.7/tutorial/index.html
   Description: A brief introduction to the main content of this getting started tutorial.
"""

"""
Python is an easy to learn, powerful programming language. 
It has efficient high-level data structures and a simple but effective approach to object-oriented programming. 
Python’s elegant syntax and dynamic typing, together with its interpreted nature, 
make it an ideal language for scripting and rapid application development in many areas on most platforms.

## Python是一种易于学习又功能强大的编程语言。
它提供了高效的高层次的数据结构，还有简单有效的面向对象编程。
Python优雅的语法和动态类型，以及解释型语言的本质，使它成为在很多领域多数平台上写脚本和快速开发应用的理想语言。##

[[ Python是一门简单易学且功能强大的编程语言。
它有着高效的高级数据结构和简单而有效的实现面向对象编程的方法。
Python的优雅语法和动态类型以及自然的解释，
使它成为编写脚本以及在大多数平台上快速开发应用的理想语言。]]

"""

"""
The Python interpreter and the extensive standard library are freely available in source or binary form 
for all major platforms from the Python Web site, https://www.python.org/, and may be freely distributed. 
The same site also contains distributions of and pointers to many free third party Python modules, 
programs and tools, and additional documentation.

## 多数平台上的 Python 解释器以及丰富的标准库的源码和可执行文件，都可以在 Python 官网 https://www.python.org/ 免费自由地下载并分享。
这个网站上也提供一些链接，包括第三方 Python 模块、程序、工具等，以及额外的文档。##

[[ Python解释器和大量的标准库以源代码或二进制的形式对所有主流的平台都免费提供，网址是https://www.python.org/，而且可以免费发布。
这个网站也包括了许多免费第三方Python模块，程序，工具和附加的文档。]]

"""

"""
The Python interpreter is easily extended with new functions and data types implemented in C or C++ 
(or other languages callable from C). Python is also suitable as an extension language for customizable applications.

## Python解释器易于扩展，可以使用C或C++（或者其他可以从C调用的语言）扩展新的功能和数据类型。Python也可用作可定制化软件中的扩展程序语言。##

[[ Python解释器易于用C或者C++的新的方法和数据类型做扩展（或者通过C调用的别的语言）。Python也适于作为一种扩展语言用在定制的应用程序中。]]
"""

"""
This tutorial introduces the reader informally to the basic concepts and features of 
the Python language and system. It helps to have a Python interpreter handy for hands-on experience, 
but all examples are self-contained, so the tutorial can be read off-line as well.

## 这个教程非正式地介绍Python语言和系统的基本概念和功能。最好在阅读的时候有一个 Python 解释器做一些练习，
不过所有的例子都是相互独立的，所以这个教程也可以离线阅读。##

[[ 这个教程为读者通俗地介绍了Python语言的基本概念和特色。它有助于用手上的Python解释器亲自动手体验一番，而且所有的例子
都包含在内，所以这个教程也可以线下阅读。]]

"""

"""
For a description of standard objects and modules, see The Python Standard Library. The Python Language Reference gives 
a more formal definition of the language. To write extensions in C or C++, read Extending and Embedding 
the Python Interpreter and Python/C API Reference Manual. There are also several books covering Python in depth.

## 有关标准的对象和模块，参阅Python标准库。Python语言参考提供了更正式的语言定义。要写C或者C++扩展，
参考扩展和嵌入Python解释器和Python/C API参考手册。也有不少书籍深入讲解 Python。##

[[ 对于标准的对象和模块，去看Python标准库。Python语言索引给出了语言更多的正式的定义。用C或C++来写扩展库时，
去读扩展和嵌入Python解释器和Python/C的API索引手册。同样有一些深度解析Python的书。]]

"""

"""
This tutorial does not attempt to be comprehensive and cover every single feature, or even every commonly used feature. 
Instead, it introduces many of Python’s most noteworthy features, and will give you a good idea of the language’s flavor 
and style. After reading it, you will be able to read and write Python modules and programs, and you will be ready to 
learn more about the various Python library modules described in The Python Standard Library.

## 这个教程并不试图完整包含每一个功能，甚至常用功能可能也没有全部涉及。这个教程只介绍 Python 中最值得注意的功能，也会让你体会到这个语言的风格特色。
学习完这个教程，你将能够阅读和编写 Python 模块和程序，也可以开始学习更多的 Python 库模块，详见 Python 标准库。##

[[ 这个教程不会试图理解和覆盖每一个单独的特点，以及甚至每一个通常用到的特点。但是，它介绍了Python最值得注意的许多特点，而且将让你很好地思考
这门语言的风格和偏好。阅读完毕之后，你将可以读写Python的模块和程序，然后你就可以准备学习用Python标准库所描述的更多的Python模块。]]

"""

"""
[VOCABULARY]
elegant: 高雅的;优雅的
extensive: 广泛的;广大的
suitable: 合适的
hands-on: 亲自动手的
self-contained: 独立的
manual: 手工的;手册
noteworthy: 值得注意的;显著的
flavor and style: 风格特色
[/VOCABULARY]
"""
