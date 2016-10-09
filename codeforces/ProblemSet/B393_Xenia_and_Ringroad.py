a=input()
b=input()

a=a.split(' ')
b=b.split(' ')
a=[int(i) for i in a]

bb=[]
bb.append(1)
for i in b:
    bb.append(int(i))
res=0
for i in range(len(bb)-1):
    if(bb[i+1]>bb[i]):
        res+=bb[i+1]-bb[i]
    elif(bb[i+1]<bb[i]):
        res+=a[0]+bb[i+1]-bb[i]
    else:
        res+=0
print(res)
