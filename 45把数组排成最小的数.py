''' ********************************************************************
    题目描述
    输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字
    中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字
    为321323。
******************************************************************** ''' 
# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        if numbers:
            n = len(str(max(numbers)))
            numbers  = list(map(str,numbers))
            s = numbers.copy()
            for i in range(len(s)):
                s[i] = [s[i]+s[i][-1]*(n-len(s[i])),i]
            s.sort()
            out = ''
            for i in range(len(s)):
                out += numbers[s[i][-1]]
            return out
        return ''
''' ********************************************************************
    解题思路：

******************************************************************** '''
if __name__ == '__main__':
    ins = Solution()
    numbers = [3,321,32]
    print(ins.PrintMinNumber(numbers))


