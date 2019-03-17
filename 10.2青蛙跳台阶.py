''' ********************************************************************
    题目描述
    一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有
    多少种跳法。
    
    # -*- coding:utf-8 -*-
    class Solution:
        def jumpFloor(self, number):
            # write code here
******************************************************************** ''' 
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, number):
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
        最后是一步登上的走法共有 f(number-1) 种，
        最后是两步登上的走法共有 f(number-2) 种。
        所以是 f(number)=f(number-1)+f(number-2)
******************************************************************** '''

