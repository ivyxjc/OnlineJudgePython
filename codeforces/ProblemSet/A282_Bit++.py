num=int(input())
res=0
for i in range(num):
    a=input();
    if(a[0]=='+'or a[-1]=='+'):
        res+=1
    else:
        res-=1

print(res)

