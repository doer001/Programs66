''' ********************************************************************
    题目描述
    给定一棵二叉搜索树，请找出其中的第k小的结点。例如，（5，3，7，2，4，6，8）中，
    按结点数值大小顺序第三小结点的值为4。
******************************************************************** ''' 
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def order(self,root):
        L = []
        if root:
            L += self.order(root.left)
            L.append(root)
            L += self.order(root.right)
        return L
    def KthNode(self, pRoot, k):
        if pRoot:
            L = self.order(pRoot)
            if 0<k<=len(L):
                return L[k-1]
        return None
''' ********************************************************************
    解题思路：

******************************************************************** '''
if __name__ == '__main__':
    pass

