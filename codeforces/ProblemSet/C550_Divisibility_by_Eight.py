input=str(input())
# print(len(input))

def getRes(input):
    for i in range(0,len(input)):
        # print("i=",input[i])
        if(int(input[i])%8==0):
            print("YES")
            print(input[i])
            return
        for j in range(i+1,len(input)):
            a=10*int(input[i])+int(input[j])
            if(a%8==0):
                print("YES")
                print(a)
                return
            for k in range(j+1,len(input)):
                # print("k=",input[k])
                b=100*int(input[i])+10*int(input[j])+int(input[k])
                if(b%8==0):
                    print("YES")
                    print(b)
                    return
    print("NO")

getRes(input)
