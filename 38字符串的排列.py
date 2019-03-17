''' ********************************************************************
    题目描述
    输入一个字符串,按字典序打印出该字符串中字符的所有排列。
    例如输入字符串abc,则打印出由字符a,b,c所能排列出来的
    所有字符串abc,acb,bac,bca,cab和cba。
******************************************************************** ''' 
# -*- coding:utf-8 -*-
import copy
class Solution:
    def __init__(self):
        self.array = []
        self.L = []
    def test(self,ss):
        if ss:
            for i in range(len(ss)):
                D = copy.copy(ss)
                self.L.append(D[i])
                del D[i]
                self.test(D)
                self.L.pop()
        else:
            self.array.append(''.join(copy.copy(self.L)))
    def Permutation(self, ss):
        if ss:
            ss = list(ss)
            self.test(ss)
            out = sorted(list(set(self.array)))
            return out
        return []
''' ********************************************************************
    解题思路：

******************************************************************** '''
if __name__ == '__main__':
    ins = Solution()
    ss = 'aba'
    print(ins.Permutation(ss))

