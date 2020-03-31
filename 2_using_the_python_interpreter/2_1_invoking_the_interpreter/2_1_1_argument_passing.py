# coding=utf-8
"""
   Filename: 2_1_1_argument_passing
   Author: Tanyee
   Date: 2020/3/26
   Original: https://docs.python.org/3.7/tutorial/interpreter.html#argument-passing
   Description: Argument passing.
"""

"""
When known to the interpreter, the script name and additional arguments thereafter are turned into a list of strings 
and assigned to the argv variable in the sys module. You can access this list by executing import sys. The length of 
the list is at least one; when no script and no arguments are given, sys.argv[0] is an empty string. When the script 
name is given as '-' (meaning standard input), sys.argv[0] is set to '-'. When -c command is used, sys.argv[0] is set 
to '-c'. When -m module is used, sys.argv[0] is set to the full name of the located module. Options found after -c 
command or -m module are not consumed by the Python interpreter’s option processing but left in sys.argv for the command
or module to handle.

## 如果可能的话，解释器会读取命令行参数，转化为字符串列表存入sys模块中的argv变量中。执行命令import sys你可以导入这个模块并访问这个列表。
这个列表最少也会有一个元素；如果没有给定输入参数，sys.argv[0] 就是个空字符串。如果脚本名是 '-'``（标准输入）时，``sys.argv[0] 就是 '-'。
使用-c 命令时，sys.argv[0]就会是'-c'。如果使用选项-m module，sys.argv[0]就是包含目录的模块全名。在-c command或-m module之后的选项
不会被解释器处理，而会直接留在sys.argv中给命令或模块来处理。##

[[ 当对解释器有所了解，脚本名字和附加的参数会转换为字符串列表，并且在sys模块分配给argv参数。你可以运行import sys得到这个列表。这个列表长度
至少为1；当不给定脚本和参数，sys.argv[0]就是一个空的字符串。当脚本名称是‘-’（即标准输入），sys.argv[0]就被设置为‘-’。当使用-c命令，
sys.argv[0]就被设置为‘-c’。当使用-m模块，sys.argv[0]就被设置为本地模块的全名。在-c或者-m后面的选项不被Python解释器选项处理，而是留给
sys.argv通过命令或模块来处理。]]
"""

"""
[VOCABULARY]
thereafter: 其后，此后
assign: 分配,指派,赋值
"""