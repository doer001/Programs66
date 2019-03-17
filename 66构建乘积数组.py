''' ********************************************************************
    题目描述
    给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素
    B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
******************************************************************** ''' 
# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        n = len(A)
        if n==0:
            return []
        if n==1:
            return [0]
        B = []
        if A.count(0) > 0:
            B = [0]*n
            if A.count(0) == 1:
                index = A.index(0)
                B[index] = 1
                for i in A:
                    if i != 0:
                        B[index] *= i
        else:
            C,D = [1],[1]
            for i in range(0,n-1):
                C.append(C[-1]*A[i])
            for i in range(n-1,0,-1):
                D.append(D[-1]*A[i])
            for i in range(n):
                B.append(C[i]*D[n-1-i])
        return B
''' ********************************************************************
    解题思路：

******************************************************************** '''
if __name__ == '__main__':
    ins = Solution()
    A = [0,0,40,0,0]
    print(ins.multiply(A))


