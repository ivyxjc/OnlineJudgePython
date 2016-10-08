class Solution(object):
    def __init__(self):
        self.map={0:'0',1: '1', 2: '2', 3: '3', 4: '4',
                  5: '5', 6: '6', 7: '7', 8: '8',
                  9: '9', 10: 'a', 11: 'b', 12: 'c',
                  13: 'd', 14: 'e', 15: 'f'}
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if(num==0):
            print(0)
            return
        tmp=num
        list1=[]
        if(tmp<0):
            tmp=-tmp-1;
        while(tmp>0):
            remainder=tmp%16
            tmp=tmp//16
            list1.append(remainder)
        # print(list1)
        strRes=['f','f','f','f','f','f','f','f']
        res=[]

        if(num>=0):

            for i in range(1,len(list1)+1):
                res.append(self.map[list1[-i]])
            return ''.join(res)
        elif(num<0):
            index=7

            for i in range(len(list1)):
                strRes[index]=self.map[15-list1[i]]
                index-=1
            return ''.join(strRes)

solution=Solution()

print(solution.toHex(26))
print(solution.toHex(-26))