''' ********************************************************************
    题目描述

******************************************************************** ''' 
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if pHead1 == None:
            return pHead2
        if pHead2 == None:
            return pHead1
        if pHead1.val < pHead2.val:
            root = pHead1
            pHead1 = pHead1.next
        else:
            root = pHead2
            pHead2 = pHead2.next
        last = root
        while pHead1 != None and pHead2 != None:
            if pHead1.val < pHead2.val:
                last.next = pHead1
                last = pHead1
                pHead1 = pHead1.next
            else:
                last.next = pHead2
                last = pHead2
                pHead2 = pHead2.next
        if pHead1!=None:
            last.next = pHead1
        if pHead2!=None:
            last.next = pHead2
        return root

''' ********************************************************************
    解题思路：

******************************************************************** '''


