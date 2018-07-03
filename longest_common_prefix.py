#-*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/longest-common-prefix/description/

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        idx = 1
        llen = len(strs)
        result = ""
        while True:
            if len(strs[0]) < idx:
                result = strs[0]
                break
            prefix = strs[0][:idx]
            for i in xrange(1, llen):
                if prefix != strs[i][:idx]:
                    return result
            result = prefix
            idx += 1
        
        return result
        
        
                
                    
                
            
    
    
s = Solution()
strs = ["flower","flow","flight"]
strs = ["dog","racecar","car"]
print s.longestCommonPrefix(strs)
