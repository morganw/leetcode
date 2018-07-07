#-*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/plus-one/description/

给定一个非负整数组成的非空数组，在该数的基础上加一，返回一个新的数组。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        stop = True
        for i in xrange(len(digits)-1, -1, -1):
            if stop is False:
                break
            d = digits[i] + 1 
            if d >= 10:
                digits[i] = d%10 
                if i == 0:
                    digits.insert(0, 1)
            else:
                digits[i] = d 
                stop = False
        
        return digits
            
            
        
    
    
s = Solution()
digits = [8,9,9]
print s.plusOne(digits)
        
        
        
        