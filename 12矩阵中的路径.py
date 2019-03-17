''' ********************************************************************
    题目描述
    请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路
    径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动
    一个格子。如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。例
    如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，
    但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个
    格子之后，路径不能再次进入该格子。
******************************************************************** ''' 
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.index=[]
    def hasPath(self, matrix, rows, cols, path): 
        L = [matrix[i*cols:(i+1)*cols] for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if L[i][j]==path[0]:
                    self.index.append([i,j])
                    if self.isPath(L,i,j,path[1:]):
                        return True
                    else:
                        self.index.pop()
        return False
    def isPath(self, L, i, j, path):
        if not path:
            return True
        for ii,jj in [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]:
            if 0<=ii<len(L) and 0<=jj<len(L[0]) and L[ii][jj]==path[0] and ([ii,jj] not in self.index):
                self.index.append([ii,jj])
                if self.isPath(L, ii, jj, path[1:]):
                    return True
                else:
                    self.index.pop()
        return False
''' ********************************************************************
    解题思路：


******************************************************************** '''

if __name__=='__main__':
    li = Solution()
    matrix, rows, cols, path = 'abcesfcsadee', 3, 4, "see"
    print(li.hasPath(matrix, rows, cols, path))
