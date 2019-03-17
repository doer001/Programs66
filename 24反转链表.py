''' ********************************************************************
    题目描述
    输入一个链表，反转链表后，输出新链表的表头。
******************************************************************** ''' 
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def ReverseList(self, pHead):
        if pHead==None:
            return
        L_node = []
        while pHead != None:
            L_node.append(pHead)
            pHead = pHead.next
        L_node = L_node[::-1]
        for i in range(len(L_node)-1):
            L_node[i].next=L_node[i+1]
        L_node[-1].next = None
        return L_node[0]
            
            
            
''' ********************************************************************
    解题思路：

******************************************************************** '''
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if pHead==None:
            return
        last = None
        while pHead:
            tmp = pHead.next
            pHead.next = last
            last = pHead
            pHead = tmp
        return last

