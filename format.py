import os
import re

def format(file):
    """
    :param file: str filename
    :return:
    """
    os.chdir("D:\\UI")
    print(os.listdir())
    with open(file,'r',encoding='utf-8') as f:
        a=f.read()
    length=len(a)

    _pattern=re.compile('---')
    _match=re.finditer(_pattern,a)
    _start1=next(_match).start()
    _start2=next(_match).start()
    a.(_start1,'<')
    print(a)


os.chdir("D:\\UI")

# for i in os.listdir():
#     if (i=='UI'):
#         if(os.path.isdir(i)):
#             os.chdir(i)
#             print(os.listdir())
#             if(os.path.isdir(i))

file='2016-09-24-ActionBar-Basic.md'
format(file)

