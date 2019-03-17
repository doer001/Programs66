''' ********************************************************************
    题目描述
    输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点
    （含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
******************************************************************** ''' 
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:                 # 非递归算法
    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        array = []
        array.append([pRoot])
        while array[-1]:
            L = []
            for i in array[-1]:
                if i.left:
                    L.append(i.left)
                if i.right:
                    L.append(i.right)
            array.append(L)
        return len(array)-1
class Solution:                 # 递归算法
    def TreeDepth(self, pRoot):
        if pRoot == None:
            return 0
        return 1 + max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right))
''' ********************************************************************
    解题思路：

******************************************************************** '''


