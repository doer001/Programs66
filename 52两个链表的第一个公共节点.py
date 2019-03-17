''' ********************************************************************
    题目描述
    输入两个链表，找出它们的第一个公共结点。
******************************************************************** ''' 
-*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        L1,L2 = [],[]
        while pHead1:
            L1.append(pHead1)
            pHead1 = pHead1.next
        while pHead2:
            L2.append(pHead2)
            pHead2 = pHead2.next
        if not L1 or not L2 or L1[-1].val!=L2[-1].val:
            return None
        i = 2
        while i<min(len(L1),len(L2))+1 and L1[-i].val == L2[-i].val:
            i += 1
        return L1[-i+1]
''' ********************************************************************
    解题思路：

******************************************************************** '''
if __name__ == '__main__':
    pass
    

