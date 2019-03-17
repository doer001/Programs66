''' ********************************************************************
    题目描述
    输出所有和为S的连续正数序列。序列内按照从小至大的顺序，
    序列间按照开始数字从小到大的顺序
******************************************************************** ''' 
# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        array = []
        i = 2
        while tsum//i*2>=i:
            if i%2!=0:
                L = list(range(tsum//i-i//2,tsum//i+i//2+1))
                if sum(L)==tsum:
                    array.append(L)
            else:
                if tsum%i != 0:
                    L = list(range(tsum//i-i//2+1,tsum//i+i//2+1))
                    if sum(L)==tsum:
                        array.append(L)
            i += 1
        array.reverse()
        return array
''' ********************************************************************
    解题思路：

******************************************************************** '''
if __name__ == '__main__':
    ins = Solution()
    tsum = 111
    print(ins.FindContinuousSequence(tsum))


