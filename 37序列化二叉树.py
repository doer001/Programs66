''' ********************************************************************
    题目描述
    请实现两个函数，分别用来序列化和反序列化二叉树
******************************************************************** ''' 
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init(self):
        self.L =[]
    def Serialize(self, root):
        L = self.order(root)
        return ','.join(L)
    def Deserialize(self, s):
        self.L = s.split(',')
        root = self.tree()
        return root
    def order(self, root):
        L = []
        if root:
            L.append(str(root.val))
            L += self.order(root.left)
            L += self.order(root.right)
        else:
            L.append('$')
        return L
    def tree(self):
        if not self.L:
            return None
        val = self.L.pop(0)
        if val == '$':
            return None
        root = TreeNode(int(val))
        root.left = self.tree()
        root.right = self.tree()
        return root
''' ********************************************************************
    解题思路：

******************************************************************** '''
if __name__ == '__main__':
    root = TreeNode(1)
    
    root.left = TreeNode(2)

    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    #root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    ins = Solution()
    s = ins.Serialize(root)
    print(s)
    print(ins.Deserialize(s))

