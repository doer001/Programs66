''' ********************************************************************
    题目描述
    给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，
    树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
******************************************************************** ''' 
# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        if pNode.right:
            r = pNode.right
            while r.left:
                r = r.left
            return r
        if pNode.next:
            h = pNode.next
            if pNode == h.left:
                return h
            else:
                hh = pNode.next.next
                if hh:
                    if h == hh.left:
                        return hh
        return None
''' ********************************************************************
    解题思路：

******************************************************************** '''
if __name__ == '__main__':
    ins = Solution()
    pass

