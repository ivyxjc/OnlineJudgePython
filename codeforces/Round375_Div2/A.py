
input=input()
input=str(input)
coordinateList=input.split(" ")
length=len(coordinateList)
coordinateList = [int(i) for i in coordinateList]

coordinateList.sort()
meeting_coordinate=coordinateList[length//2]
res=0
for i in coordinateList:
    res+=abs(int(i)-int(meeting_coordinate))
print(res)
