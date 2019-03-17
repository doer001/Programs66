''' ********************************************************************
    题目描述
    输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
    使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
    并保证奇数和奇数，偶数和偶数之间的相对位置不变。
    
    # -*- coding:utf-8 -*-
    class Solution:
        def reOrderArray(self, array):
            # write code here
******************************************************************** ''' 
import time
class Solution:
    def reOrderArray(self, array):
        L,R = [],[]
        for i in array:
            if i%2==1:
                L.append(i)
            else:
                R.append(i)
        L.extend(R)
        return L

''' ********************************************************************
    解题思路：
        以空间换时间, L.extend(R) 比 L+R 要快
******************************************************************** '''
li=Solution()
array = list(range(1000))
time1 = time.time()
for i in range(10000):
    li.reOrderArray(array)
time2 = time.time()
print(time2-time1)

