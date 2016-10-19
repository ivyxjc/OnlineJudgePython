class Solution(object):

    def __init__(self):
        self.hour=[1,2,4,8]
        self.minute=[1,2,4,8,16,32]
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        # res=[]
        # for i in range(num):
        #     hourSum=self.sumNum(i,'hour')
        #     minuteSum=self.sumNum(num-i,'minue')
        #
        # res=self.combine(hourSum,minuteSum)
        print(self.combine([1,2,3],[2,3,4]))


    def sumNum(self,num,flag):

        """
        某一数组内num个数字相互组合的所有情况
        :param num: int
        :param flag:  str 'minute' or 'hour'
        :return: list[int]
        """
        pass


    def combine(self,hour,minute):
        """
        两个数组各取1个数组合的所有情况
        :param hour:  list[int]
        :param minute:  list[int]
        :return:    list[list[int]]
        """
        res=[]
        for i in hour:  
            for j in minute:
                res.append([i,j])
        return res

    def format(self,list):
        """
        格式化最终结果
        :param list:
        :return:
        """

sol=Solution()
sol.readBinaryWatch(4)