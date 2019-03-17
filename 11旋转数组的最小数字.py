''' ********************************************************************
    题目描述
    把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 
    输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。 
    例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 
    NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
    
    # -*- coding:utf-8 -*-
    class Solution:
        def minNumberInRotateArray(self, rotateArray):
            # write code here
******************************************************************** ''' 
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if rotateArray==[]:
            return 0
        else:
            min = rotateArray[0]
            for i in rotateArray:
                if i<min:
                    min=i
            return min
''' ********************************************************************
    解题思路1：
    遍历所有的数，找到最小的一个
******************************************************************** '''
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        n = len(rotateArray)
        if n==0:
            return 0
        else:
            for i in range(1,n):
                if rotateArray[i]<rotateArray[i-1]:
                    return rotateArray[i]
            return rotateArray[0]
''' ********************************************************************
    解题思路2：
    因为数组是循环非减有序的，所以如果后面的数比前面的数还小，肯定是最小的，
    但是如果所有的数都一样，则返回第一个数
******************************************************************** '''
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        length = len(rotateArray)
        if length == 0:return 0
        if length == 1:return rotateArray[0]
        left, right = 0, length- 1
        while left<= right:
            mid = (left+ right) >> 1
            if rotateArray[mid] > rotateArray[right]:left = mid+ 1
            elif rotateArray[mid] < rotateArray[right]:right = mid
            else:right -= 1
            if left >= right:break
        return rotateArray[left]
''' ********************************************************************
    解题思路3：
    如果数组为空，则返回0；
    如果数组中只有一个数，则返回这个数；
    如果数组中不止一个数，则判断两边与中间的数的值：
        如果最右边的数<中间的数，说明后面这段是递增的，最小数肯定不在后面
        如果中间的数>最右边的数，说明最小数肯定在后面
        如果中间的数=右边的数，说明从中间到最后都相同，从中间在往左面取值
    当左边和右边指向同一个数时，则说明找到了这个数
    ！说明：
        跟右边的数进行比较是有原因的，如果只有两数的时候，mid=(0+1)//2=0=left,
        所以没办法跟左边比较
******************************************************************** '''

