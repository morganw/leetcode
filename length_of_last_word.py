#-*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/length-of-last-word/description/

给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指由字母组成，但不包含任何空格的字符串。

示例:

输入: "Hello World"
输出: 5
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if not s:
            return 0 
        
        result = 0
        for i in xrange(len(s)-1, -1, -1):
            if s[i] == " ":
                break
            result += 1
        
        return result
        





s = Solution()
ss = "Hello World"
print s.lengthOfLastWord(ss)
        
        
        
        
        
        
        
        
        