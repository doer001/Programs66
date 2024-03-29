''' ********************************************************************
    题目描述
    HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。
    今天测试组开完会后,他又发话了:在古老的一维模式识别中,
    常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。
    但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？
    例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。
    给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)
******************************************************************** ''' 
# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        n = len(array)
        max_sum = array[0]
        for i in range(1,n+1):
            for j in range(n+1-i):
                sum_i = sum(array[j:j+i])
                if sum_i > max_sum:
                    max_sum = sum_i
        return max_sum

''' ********************************************************************
    解题思路：
    最笨的方法是遍历，1个数，2个数，...n个数的和，但是这么常规的解法是拿不到offer
******************************************************************** '''
# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if not array:                 # 如果序列为空，则返回空
            return 
        max_sum = sum_part = array[0] # 统计从第一个数开始
        for i in range(1,len(array)):
            if sum_part < 0:          # 如果序列和小于0，则此序列没有叠加的必要
                sum_part = array[i]
            else:                     # 如果序列和大于0，继续叠加
                sum_part += array[i]
            if sum_part > max_sum:    # 在叠加的过程中记录最大值
                max_sum = sum_part
        return max_sum

