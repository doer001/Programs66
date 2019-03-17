# -*- coding:utf-8 -*-
'''
    题目描述
    给定一个double类型的浮点数base和int类型的整数exponent。
    求base的exponent次方。
    class Solution:
        def Power(self, base, exponent):
            # write code here
'''
class Solution:
    def Power(self, a, b):
        #return base**exponent 用这句是拿不到offer的
        if b==0:
            return 1
        elif a==0 and b<0:
            return False
        elif b<0:
            a,b = 1/a,-b
        num = 1
        for i in range(b):
            num *= a
        return num
li = Solution()
print(li.Power(0,0))
print(li.Power(0,-1))
print(li.Power(2,-5))
print(li.Power(-2,-5))
print(li.Power(-2,5))
print(li.Power(2,5))
print(li.Power(0,3))

            
