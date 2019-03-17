''' ********************************************************************
    题目描述
    输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
    路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
******************************************************************** ''' 
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.array = []
        self.L = []

    def path(self,root):
        if root:
            self.L.append(root.val)
        if root.left==None and root.right==None:
            #self.array.append(self.L)           # 注意此语句得不到想要的结果
            M = self.L.copy()                   
            self.array.append(M)
            
        if root.left and root.right==None:
            self.path(root.left)
        if root.left==None and root.right:
            self.path(root.right)
        if root.left and root.right:
            self.path(root.left)
            self.L.pop()
            self.path(root.right)
            self.L.pop()
            
    def FindPath(self, root, expectNumber):
        L = []
        if root:
            self.path(root)
            for i in self.array:
                if sum(i)==expectNumber:
                    L.append(i)
        return L

''' ********************************************************************
    解题思路：

******************************************************************** '''
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    ins = Solution()
    ins.path(root)
    print(ins.array)

