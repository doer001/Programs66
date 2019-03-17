''' ********************************************************************
    题目描述
    地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，
    右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 
    例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不
    能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
******************************************************************** ''' 
# -*- coding:utf-8 -*-
class Solution:
    def sum_xy(self,x,y):
        sum = 0
        while x//10 or x%10:
            sum += x%10
            x //= 10
        while y//10 or y%10:
            sum += y%10
            y //= 10
        return sum
    def movingCount(self, z, x, y):
        if z<0:
            return 0
        D =[[0,0]]
        L = [[[0,0]]]
        i = 0
        while(i<=x+y-2):        # 第i步，最长x+y-2步
            if L[-1]:
                L.append([])
            for d in L[-2]:
                if d[0]+1<x and self.sum_xy(d[0]+1,d[1])<=z:
                    if [d[0]+1,d[1]] not in D:
                        L[-1].append([d[0]+1,d[1]])
                        D.append([d[0]+1,d[1]])
                if d[0]-1>=0 and self.sum_xy(d[0]-1,d[1])<=z:
                    if [d[0]-1,d[1]] not in D:
                        L[-1].append([d[0]-1,d[1]])
                        D.append([d[0]-1,d[1]])
                if d[1]+1<y and self.sum_xy(d[0],d[1]+1)<=z:
                    if [d[0],d[1]+1] not in D:
                        L[-1].append([d[0],d[1]+1])
                        D.append([d[0],d[1]+1])
                if d[1]-1>=0 and self.sum_xy(d[0],d[1]-1)<=z:
                    if [d[0],d[1]-1] not in D:
                        L[-1].append([d[0],d[1]-1])
                        D.append([d[0],d[1]-1])
            if L[-1]==[]:
                break
            i+=1
        return len(D)
''' ********************************************************************
    解题思路：

******************************************************************** '''
if __name__ == '__main__':
    ins = Solution()
    x,y,z = 10,10,5
    print(ins.movingCount(z, x, y))

