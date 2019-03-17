''' ********************************************************************
    题目描述
    输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
    如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
******************************************************************** ''' 
class Solution:
    def test(self, l):
        n = len(l)
        if n<=1:
            return True
        for i in range(n):
            if l[i]>=l[-1]:
                left,right = l[:i],l[i:-1]
                break
        if right and min(right)<l[-1]:
            return False
        if self.test(left) and self.test(right):
            return True
        else:
            return False
    def VerifySquenceOfBST(self, sequence):
        if sequence and self.test(sequence):
            return True
        return False
''' ********************************************************************
    解题思路：
    BST的后序序列的合法序列是，对于一个序列S，最后一个元素是x （也就是根），
    如果去掉最后一个元素的序列为T，那么T满足：T可以分成两段，前一段（左子树）小于x，
    后一段（右子树）大于x，且这两段（子树）都是合法的后序序列。完美的递归定义:)。
    注意！题中sequence=[]的情况判断为False，但是在子树中的判断应该为True
******************************************************************** '''


