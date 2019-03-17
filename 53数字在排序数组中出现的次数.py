''' ********************************************************************
    题目描述
    输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，
    则最小的4个数字是1,2,3,4,。
******************************************************************** ''' 
# -*- coding:utf-8 -*-
class Solution:
    def GetNumber(self, data, k):
        if data:
            left,right = 0 ,len(data)-1
            while left!=right:
                mid = (left+right)//2
                if k == data[mid]:
                    return mid
                elif k > data[mid]:
                    left = mid+1
                else:
                    right = mid
            if data[left]==k:
                return left
        return 'NO'        # 不能返回False，因为会存在脚标为0的情况，而0==Fasle
    def GetNumberOfK(self, data, k):
        index = self.GetNumber(data,k)
        if index != 'NO':
            n = 1
            for i in range(index+1,len(data)):
                if data[i]==k:
                    n+=1
                else:
                    break
            for i in range(index-1,-1,-1):
                if data[i]==k:
                    n+=1
                else:
                    break
            return n
        return 0
''' ********************************************************************
    解题思路：

******************************************************************** '''


