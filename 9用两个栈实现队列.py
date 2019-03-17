''' ********************************************************************
    题目描述
    用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
    
    # -*- coding:utf-8 -*-
    class Solution:
        def push(self, node):
            # write code here
        def pop(self):
            # return xx
******************************************************************** ''' 
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def push(self, node):
        self.stack1.append(node)
    def pop(self):
        if self.stack2==[]:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        return self.stack2.pop()
''' ********************************************************************
    解题思路1：
    先把数据压入栈1，然后从栈1弹出数据压入栈2，这样数据存入栈1的时候是后入先出的，
    但是数据在栈2中是相对于压入栈1的数据的次序是先入先出的
******************************************************************** '''

