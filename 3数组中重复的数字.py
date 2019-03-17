# -*- coding:utf-8 -*-

''' ********************************************************************
    题目描述
    在一个长度为n的数组里的所有数字都在0到n-1的范围内。
    数组中某些数字是重复的，但不知道有几个数字是重复的。
    也不知道每个数字重复几次。请找出数组中任意一个重复的数字。
    例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，
    那么对应的输出是第一个重复的数字2。
    
    # -*- coding:utf-8 -*-
    class Solution:
        # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
        # 函数返回True/False
        def duplicate(self, numbers, duplication):
            # write code here
******************************************************************** ''' 
# -*- coding:utf-8 -*-
class Solution:
    def duplicate(self, numbers, duplication):
        hash = dict()
        for num in numbers:
            if(num in hash):
                duplication[0]=num
                return True
            else:
                hash[num]=1
        return False
''' ********************************************************************
    解题思路1
    从头到尾按顺序扫描数组,每扫描一个数，判断是否在哈希表中，如果是，就找到了这个重
    复的数字，否则，就把这个数加入到哈希表中
    时间复杂度=O(n),空间复杂度=O(n)
******************************************************************** '''
# -*- coding:utf-8 -*-
class Solution:
    def duplicate(self, numbers, duplication):
        n = len(numbers)
        for i in range(n):
            for j in range(i+1,n):
                if(numbers[i]==numbers[j]):
                    duplication[0]=numbers[i]
                    return True
        return False
''' ********************************************************************
    解题思路2
    从第一个数开始与后面的数进行比较，如果后面有相同的数，则找到这个重复的数字。
    时间复杂度=O(n^2),空间复杂度=O(1)
******************************************************************** '''
# -*- coding:utf-8 -*-
class Solution:
    def duplicate(self, numbers, duplication):
        numbers.sort()
        n = len(numbers)
        for i in range(n-1):
            if(numbers[i]==numbers[i+1]):
                duplication[0]=numbers[i]
                return True
        return False
''' ********************************************************************
    解题思路3
    先给数组排序，然后从头到尾检查连续的两个数是否相同，如果相同则找到重复数字。
    时间复杂度=,空间复杂度=
******************************************************************** '''
