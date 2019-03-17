''' ********************************************************************
    题目描述
    输入一个链表，输出该链表中倒数第k个结点。
******************************************************************** ''' 
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        n = 0
        cur =head
        while cur != None:
            n += 1
            cur = cur.next
        if n==0 or k<1 or k>n:
            return None
        else:
            cur =head
            for i in range(n-k):
                cur = cur.next
            return cur
                
''' ********************************************************************
    解题思路：
    先获取链表的长度n。如果链表长度为0，或者k不是大于0的数，或者k大于链表的长度，
    则没有对应的节点。否则获取第n-k+1个节点
    
******************************************************************** '''
class Solution:
    def FindKthToTail(self, head, k):
        L = []  # 存放链表节点的列表
        while head != None:
            L.append(head)
            head = head.next
        if len(L)==0 or k<1 or k>len(L):
            return None
        return L[-k]
''' ********************************************************************
    解题思路2：
    在解题思路1的基础上进行优化，以空间换时间，只需遍历一遍即可
    
******************************************************************** '''
