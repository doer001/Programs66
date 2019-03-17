''' ********************************************************************
    题目描述
    输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
    要求不能创建任何新的结点，只能调整树中结点指针的指向。
******************************************************************** ''' 
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Order(self, root):
        L = []
        if root:
            L += self.Order(root.left)
            L.append(root)
            L += self.Order(root.right)
        return L
    def Convert(self, root):
        if root and (root.left or root.right):
            NodeList = self.Order(root)
            for i in range(1,len(NodeList)-1):
                NodeList[i-1].right = NodeList[i]
                NodeList[i].left = NodeList[i-1]
                NodeList[i].right = NodeList[i+1]
                NodeList[i+1].left = NodeList[i]
            return NodeList[0]
        return root
''' ********************************************************************
    解题思路：

******************************************************************** '''
if __name__ == '__main__':
    pass

