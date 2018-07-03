#-*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/reverse-integer/description/

给定一个 32 位有符号整数，将整数中的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21

"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return  0 
        
        result = 0
        flag = 1
        if x < 0:
            flag = -1
        x= abs(x)
        while x > 0:
            result = result * 10 + x%10
            x = x/10
            
        result = result*flag
        if result < -2**31 or result > 2**31 -1:
            result = 0
        
        return result
    
    
s = Solution()
x = 120
print s.reverse(x)
