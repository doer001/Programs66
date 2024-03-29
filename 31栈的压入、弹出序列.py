''' ********************************************************************
    题目描述
    输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的
    弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，
    序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序
    列的弹出序列。（注意：这两个序列的长度是相等的）
******************************************************************** ''' 
# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        n = len(pushV)
        stack=[]
        j=0
        for i in range(n):
            stack.append(pushV[i])
            if stack[-1]==popV[j]:
                stack.pop()
                j+=1
        for i in range(j,n):
            if popV[i]!=stack[-1]:
                return False
            stack.pop()
        return True
''' ********************************************************************
    解题思路：
    BST的后序序列的合法序列是，对于一个序列S，最后一个元素是x （也就是根），
    如果去掉最后一个元素的序列为T，那么T满足：T可以分成两段，前一段（左子树）小于x，
    后一段（右子树）大于x，且这两段（子树）都是合法的后序序列。完美的递归定义:)。
    注意！题中sequence=[]的情况判断为False，但是在子树中的判断应该为True
******************************************************************** '''


