''' ********************************************************************
    题目描述
    现在要求输入一个整数n，请你输出斐波那契数列的第n项。
    第0项为0，第一项为1，以后每项为前两项之和。
    
    # -*- coding:utf-8 -*-
    class Solution:
        def Fibonacci(self, n):
            # write code here
******************************************************************** ''' 
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        if(n<2):
            return n
        else:
            fn,fn_1 = 1,0
            for i in range(2,n+1):
                fn,fn_1 = fn+fn_1,fn
            return fn
''' ********************************************************************
    解题思路1：

******************************************************************** '''

