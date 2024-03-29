''' ********************************************************************
    题目描述
    操作给定的二叉树，将其变换为源二叉树的镜像。
******************************************************************** ''' 
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Mirror(self, root):
        if root is None:
            return 
        root.left,root.right = root.right,root.left
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root
''' ********************************************************************
    解题思路：
    递归，先对跟节点镜像，然后对左子树镜像，再对右子树镜像
******************************************************************** '''


