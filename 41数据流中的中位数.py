''' ********************************************************************
    题目描述
    如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是
    所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就
    是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，
    使用GetMedian()方法获取当前读取数据的中位数。
******************************************************************** ''' 
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.data = []
    def Insert(self, num):
        self.data.append(num)
        self.data.sort()
    def GetMedian(self,data):
        n = len(self.data)
        if n%2!=0:
            return self.data[n//2]
        return (self.data[n//2-1]+self.data[n//2])/2.0
''' ********************************************************************
    解题思路：

******************************************************************** '''
if __name__ == '__main__':
    ins = Solution()
    L = [3,2,6,4,9,5,1,7,8]
    for i in L:
        ins.Insert(i)
        print(ins.data)
        print(ins.GetMedian(i))

