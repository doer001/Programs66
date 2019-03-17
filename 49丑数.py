''' ********************************************************************
    题目描述
    把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，
    因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
******************************************************************** ''' 
# -*- coding:utf-8 -*-
'''
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index>0:
            m2 = [1]
            for i in range(index-1):
                temp = m2[-1]*2
                for i in range(len(m2)-2, -1, -1):
                    if m2[-1] < m2[i]*2 < temp:
                        temp = m2[i]*2
                    if m2[-1] < m2[i]*3 < temp:
                        temp = m2[i]*3
                    if m2[-1] < m2[i]*5 < temp:
                        temp = m2[i]*5
                    if m2[i]*5 <= m2[-1]:
                        break
                m2.append(temp)
            return m2[-1]
        return 0
'''
'''
class Solution:
    def IsUgly(self, num):
        while num%2 == 0:
            num //= 2
        while num%3 == 0:
            num //= 3
        while num%5 == 0:
            num //= 5
        if num == 1:
            return True
        return False
    def GetUglyNumber_Solution(self, index):
        if index>0:
            m2 = []
            i = 1
            while len(m2)<index:
                if self.IsUgly(i):
                    m2.append(i)
                i += 1
            return m2
        return 0
'''
class Solution:
    def GetUglyNumber_Solution(self, index):
        if (index <= 0):
            return 0
        L = [1]
        m2,m3,m5 = 0,0,0
        for i in range(index-1):
            num = min(L[m2]*2, L[m3]*3, L[m5]*5)
            L.append(num)
            if num % 2 == 0:
                m2 += 1
            if num % 3 == 0:
                m3 += 1
            if num % 5 == 0:
                m5 += 1
        return L
''' ********************************************************************
    解题思路：

******************************************************************** '''
if __name__ == '__main__':
    ins = Solution()
    index = 100
    print(ins.GetUglyNumber_Solution(index))

