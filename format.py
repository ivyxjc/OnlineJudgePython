import os
import re


def format(file):
    """
    :param file: str filename
    :return:
    """
    with open(file, 'r', encoding='utf-8')    as f:
        a = f.read()
    length=len(a)

    datePattern=re.compile('\d\d\d\d-\d+-\d+')
    dateMatch=re.search(datePattern,str(file))

    _pattern=re.compile('---')
    _match=re.finditer(_pattern,a)

    try:
        _start1=next(_match).start()
        _start2=next(_match).start()
        a=replace(a,_start1,_start1+1,'<!')
        a=replace(a,_start2+3,_start2+4,'>')
    except StopIteration:
        print(file+ " _ not match")



    dataPattern=re.compile('data:\s+\d\d\d\d')
    dataMatch=re.search(dataPattern,a)
    if (dataMatch is not None):

        a=replace(a,dataMatch.start()+3,dataMatch.start()+4,'e')
    else:
        print(file+ " data not match")


    layoutPattern=re.compile('layout: post')
    layoutMatch=re.search(layoutPattern,a)
    if(layoutMatch is not None):
        a=replace(a,layoutMatch.start(),layoutMatch.end(),'author: ivyxjc\ndate: '+file[dateMatch.start():dateMatch.end()])
    else:
        print(file+ " layout not match")

    tagsPattern=re.compile('tags:(.*)\n')
    tagsMatch=re.search(tagsPattern,a)
    tags=a[tagsMatch.start():tagsMatch.end()]
    if(re.search(re.compile('\['),tags)):
        bracketLeft=re.search(re.compile('\['),tags)
        tags=replace(tags,bracketLeft.start(),bracketLeft.start()+1,'')
        bracketRight=re.search(re.compile(']'),tags)
        tags=replace(tags,bracketRight.start(),bracketRight.start()+1,'')
        a=replace(a,tagsMatch.start(),tagsMatch.end(),tags+'status: publish\n')
    else:
        pass

    keywordsPattern=re.compile('keywords:')
    keyMatch=re.search(keywordsPattern,a)
    if(keyMatch is not None):
        a=replace(a,keyMatch.start(),keyMatch.end()+1,'')
    else:
        print(file + " key not match")

    descriPattern=re.compile('description:')
    descriMatch=re.search(descriPattern,a)
    if(descriMatch is not None):
        a=replace(a,descriMatch.start(),descriMatch.end(),'summary: ')
    else:
        print(file + " description not match")


    with open(file,'w',encoding='utf-8') as f:
        f.write(a)

def replace(str,start,end,ss):
    """
    将[start:end](包括start和end)替换为ss
    :param str:
    :param start:  int
    :param end:    int
    :param ss:
    :return:
    """
    return str[:start]+ss+str[end:]

# format('D:\\new\\OJ\\LeetCode\\2016-04-21-medium-SingleNum.md')

def make(baseDir):
    listdir = os.listdir(baseDir)
    os.chdir(baseDir)
    for i in listdir:
        i=os.path.abspath(i)
        print(i)
        if(not os.path.isdir(i)):
            format(i)
            print("format  "+i)
        else:
            make(os.path.abspath(i))
            os.chdir(baseDir)

make('D:\\new')


