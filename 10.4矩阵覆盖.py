''' ********************************************************************
    题目描述
    我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
    请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
    
    # -*- coding:utf-8 -*-
    class Solution:
        def rectCover(self, number):
            # write code here
******************************************************************** ''' 
# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        if(number<3):
            return number
        else:
            fn,fn_1 = 2,1
            for i in range(3,number+1):
                fn,fn_1 = fn+fn_1,fn
            return fn
''' ********************************************************************
    解题思路：
    当 number=1 时，f=1；
    当 number=2 时，f=2；
    当 n>3 时：
        最后一块是2*1的矩形的情况共有 f(number-1) 种，
        而最后一块是(1*2)*2的矩形的情况共有 f(number-2) 种。
        所以 f(number)=f(number-1)+f(number-2)
******************************************************************** '''

