''' ********************************************************************
    题目描述
    从上往下打印出二叉树的每个节点，同层节点从左至右打印。层序遍历
******************************************************************** ''' 
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        if pRoot==None:
            return []
        array = [[pRoot]]
        while array[-1]:
            L = []
            for i in array[-1]:
                if i.left:
                    L.append(i.left)
                if i.right:
                    L.append(i.right)
            array.append(L)
        out = []
        for i in array:
            if i:
                out.append([])
                for j in i:
                    out[-1].append(j.val)
        for i in range(len(out)):
            if i%2==1:
                out[i].reverse()
        return out
''' ********************************************************************
    解题思路：

******************************************************************** '''

