''' ********************************************************************
    题目描述
    输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
    
    # -*- coding:utf-8 -*-
    # class ListNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None

    class Solution:
        # 返回从尾部到头部的列表值序列，例如[1,2,3]
        def printListFromTailToHead(self, listNode):
            # write code here
******************************************************************** ''' 
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        arrayList = []
        while(listNode):
            arrayList.append(listNode.val)
            listNode = listNode.next
        return arrayList[::-1]
        #return list(reversed(arrayList))
''' ********************************************************************
    解题思路1：

******************************************************************** '''

