strlen=int(input())
str=input()


def get_split_content(str,strlen,left_separator,right_separator):
    """
    将左右分隔符中间及以外的内容分开
    """
    in_parentheses = []
    out_parentheses = []
    index = 0
    left_flag = 0
    while(True):
        if(index>=strlen):
            break
        if(str[index]== left_separator):
            out_parentheses.append(left_separator)
            left_flag+=1
            while(True):
                index+=1
                if(str[index]==left_separator):
                    left_flag+=1
                    out_parentheses.append(left_separator)
                    continue
                if(str[index]== right_separator):
                    left_flag-=1
                    in_parentheses.append(str[index])
                    index+=1
                    if (left_flag == 0):
                        break
                in_parentheses.append(str[index])
        else:
            if (index >= strlen):
                break
            out_parentheses.append(str[index])
            index += 1
    return in_parentheses,out_parentheses


def get_words(out_parentheses,separtor=['_','(']):
    """
    获取一个字符list中，被分隔符隔开的单词，并输出单词list
    """
    index_out=0
    out_words=[]
    out_words_index=0;

    while(True):
        if(index_out>=len(out_parentheses)):
            break
        if(out_parentheses[index_out] not in separtor):
            out_words.append([])
            while(True):
                if(out_parentheses[index_out] in separtor):
                    break
                out_words[out_words_index].append(out_parentheses[index_out])
                index_out+=1
                if (index_out >= len(out_parentheses)):
                    break
            out_words_index+=1
        index_out+=1
    return out_words



in_parentheses,out_parentheses = get_split_content(str,strlen,'(',')')
out_words=get_words(out_parentheses)

max_num=0
for i in out_words:
    length=len(i)
    if(length>max_num):
        max_num=length

in_parentheses_num=0
index_in=0
while(True):
    if(index_in>=len(in_parentheses)):
        break
    if (in_parentheses[index_in]!='_' and in_parentheses[index_in]!=')'):
        while(True):
            index_in+=1
            if (index_in >= len(in_parentheses)):
                break
            if(in_parentheses[index_in]==')'or in_parentheses[index_in]=='_'):
                break
        in_parentheses_num+=1
    index_in+=1


print(max_num)
print(in_parentheses_num)

