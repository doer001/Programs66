''' ********************************************************************
    题目描述
    输入两棵二叉树A，B，判断B是不是A的子结构。
    （ps：我们约定空树不是任意一个树的子结构）
******************************************************************** ''' 
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def part(self, root1, root2):
        if root2.left:          # 如果B树的左节点存在 
            if root1.left==None or root1.left.val != root2.left.val:
                return False    # 如果A树的左节点不存在，或A,B左节点的值不同，返回0
            elif self.part(root1.left, root2.left)==False:
                return False    # 如果B的左子树不是A的左子树的上半部分，返回0
        if root2.right:         # 如果B树的右节点存在 #
            if root1.right==None or root1.right.val != root2.right.val:
                return False    # 如果A树的右节点不存在，或A,B右节点的值不同 #
            elif self.part(root1.right, root2.right)==False:
                return False    # 如果B的右子树不是A的右子树的上半部分，返回0
        return True             # 如果前面都符合，则说明B树是A树的上半部分

    def HasSubtree(self, pRoot1, pRoot2):
        if pRoot2==None or pRoot1==None:    # 如果B树为空，则返回0 #
            return False                    # 如果B树不为空，且A树为空，则返回0 #
        if pRoot2.val == pRoot1.val and self.part(pRoot1, pRoot2):
            return True         # 如果A,B树根节点的值相同，且B是A的上半部分，返回1
        if self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2):
            return True        # 判断B树是否是A的左右子树的子结构，如果是则返回1，否则返回0
        else:
            return False
''' ********************************************************************
    解题思路：

******************************************************************** '''
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root2 = root.left
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    ins = Solution()
    print(ins.HasSubtree(root, root2))

