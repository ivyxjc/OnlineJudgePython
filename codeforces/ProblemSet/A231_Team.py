num=int(input())
res=0
for i in range(num):
    a=input()
    a=a.split(' ')
    a=[int(j) for j in a]
    # print(a)
    flag=0
    for j in a:
        flag+=j
    if(flag>=2):
        res+=1
print(res)
