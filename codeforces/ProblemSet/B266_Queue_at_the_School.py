def swap(i,j):
    tmp=line[i]
    line[i]=line[j]
    line[j]=tmp

a=input()
line=input()
a=a.split(' ')
num=a[0]
time=int(a[1])
line=[i for i in line]

while(time>0):
    time-=1
    flagBoy=False
    for i in range(len(line)):
        if(line[i]=='B'):
            flagBoy=True
        if(flagBoy and line[i]=='G'):
            swap(i-1,i)
            flagBoy=False
print(''.join(line))


