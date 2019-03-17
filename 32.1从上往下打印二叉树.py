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
    def PrintFromTopToBottom(self, root):
        if not root:
            return []
        L = []            # 用来存放每层节点列表
        L.append([root])  # 先加入根节点
        while True:
            temp=[]
            for i in L[-1]:
                if i.left != None:
                    temp.append(i.left)
                if i.right != None:
                    temp.append(i.right)
            if len(temp)==0:    # 如果没有数据加入层节点列表
                break           # 结束循环
            else:
                L.append(temp)   # 加入层节点列表
        L_out=[]
        for i in L:
            for j in i:
                L_out.append(j.val)
        return L_out

''' ********************************************************************
    解题思路：

******************************************************************** '''
class Solution:
    def PrintFromTopToBottom(self, root):
        if not root:
            return []
        L_out = []
        layer = [root]
        while(len(layer)):
            temp = layer.pop(0)
            L_out.append(temp.val)
            if temp.left:
                layer.append(temp.left)
            if temp.right:
                layer.append(temp.right)
        return L_out
