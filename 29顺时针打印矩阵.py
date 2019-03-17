''' ********************************************************************
    题目描述
    输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如
    下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字
    1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
******************************************************************** ''' 
# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        m,n = len(matrix),len(matrix[0])
        if n==1:                            # 如果只有一列，直接输出此列
            return [i[0] for i in matrix]
        if m==1:                            # 如果只有一行，直接输出此行
            return matrix[0]
        if m==2:                            # 如果只有两行，直接输出两行
            return matrix[0]+list(reversed(matrix[1]))
        # 如果大于2行1列，则可遍历一圈，然后加上内部递归后的结果
        L = matrix[0]                       # 用来存放输出列表
        for i in range(1,m):
            L.append(matrix[i][-1])
        for i in range(n-2,-1,-1):
            L.append(matrix[-1][i])
        for i in range(m-2,0,-1):
            L.append(matrix[i][0])
        Mat = []                    # 用来存放子区域
        for i in range(1,m-1):
            Mat.append(matrix[i][1:n-1])
        if len(Mat[0]):
            return L+self.printMatrix(Mat)
        return L
''' ********************************************************************
    解题思路：

******************************************************************** '''


