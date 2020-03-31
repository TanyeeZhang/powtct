# coding=utf-8
"""
   Filename: 2_2_1_source_code_encoding
   Author: Tanyee
   Date: 2020/3/26
   Description: https://docs.python.org/3.7/tutorial/interpreter.html#source-code-encoding
"""

"""
By default, Python source files are treated as encoded in UTF-8. In that encoding, characters of most languages in the 
world can be used simultaneously in string literals, identifiers and comments — although the standard library only uses 
ASCII characters for identifiers, a convention that any portable code should follow. To display all these characters 
properly, your editor must recognize that the file is UTF-8, and it must use a font that supports all the characters in 
the file.

## 默认情况下，Python 源码文件以UTF-8编码方式处理。在这种编码方式中，世界上大多数语言的字符都可以同时用于字符串字面值、变量或函数名称
以及注释中——尽管标准库中只用常规的ASCII字符作为变量或函数名，而且任何可移植的代码都应该遵守此约定。要正确显示这些字符，你的编辑器必须能
识别UTF-8编码，而且必须使用能支持打开的文件中所有字符的字体。##

[[ Python默认源文件一直被看做用UTF-8编码的。使用UTF-8编码，世界上大多数语言的字符会同时用作字符串文字、标识符和注释——虽然标准库只用了
ASCII码作为标识符，但这是任何便携式代码需要遵守的。为了正确展示这些字符，你的编辑器必须能识别文件的格式是UTF-8，并且必须使用一种支持
所有文件中字符的字体。]]
"""
"""
To declare an encoding other than the default one, a special comment line should be added as the first line of the file.
The syntax is as follows:

## 如果不使用默认编码，要声明文件所使用的编码，文件的第一行要写成特殊的注释。语法如下所示：##

[[ 为了声明非默认的新的编码格式，需要添加一行特殊的注释语句在文件的第一行，语法如下所示：]]

"""

"""
# -*- coding: encoding -*-
"""

"""
where encoding is one of the valid codecs supported by Python.

## 其中encoding可以是Python支持的任意一种codecs。##

[[ 其中encoding是Python支持的codecs中的一种。]]
"""

"""
For example, to declare that Windows-1252 encoding is to be used, the first line of your source code file should be:

## 比如，要声明使用Windows-1252编码，你的源码文件要写成：##

[[ 例如，声明将使用Windows-1252编码，你的源代码第一行就会是：]]
"""

"""
# -*- coding: cp1252 -*-
"""

"""
One exception to the first line rule is when the source code starts with a UNIX “shebang” line. In this case, 
the encoding declaration should be added as the second line of the file. For example:

## 关于第一行规则的一种例外情况是，源码以UNIX "shebang" 行开头。这种情况下，编码声明就要写在文件的第二行。例如##

[[ 第一行规则有个例外是当源代码以UNIX “shebang”句开始，在这个例子中，编码格式的声明应该被加到文件的第二行。例如：]]
"""

"""
#!/usr/bin/env python3
# -*- coding: cp1252 -*-
"""

"""
[VOCABULARY]
simultaneously: 同时地
identifier: 标识符;识别码
convention: 会议;习俗;公约
portable: 便携的;可移植的
valid: 有效的
"""