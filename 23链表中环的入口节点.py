''' ********************************************************************
    题目描述
    给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
******************************************************************** ''' 
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        L= []
        while pHead and pHead not in L:
            L.append(pHead)
            pHead = pHead.next
        if pHead:
            return pHead
        return None
''' ********************************************************************
    解题思路：

******************************************************************** '''
if __name__ == '__main__':
    pass

