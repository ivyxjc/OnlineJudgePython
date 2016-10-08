map={
    "monday":1,
    "tuesday":2,
    "wednesday":3,
    "thursday":4,
    "friday":5,
    "saturday":6,
    "sunday":7
}
a=input()
b=input()

a_int=map.get(a)
b_int=map.get(b)

if(a_int==b_int):
    print("YES")
elif(b_int-a_int==3 or b_int+7-a_int==3):
    print("YES")
elif (b_int-a_int==2 or b_int+7-a_int==2):
    print("YES")
else:
    print("NO")