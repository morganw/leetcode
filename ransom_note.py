#-*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/ransom-note/description/

给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。如果可以构成，返回 true ；否则返回 false。

(题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。)

注意：

你可以假设两个字符串均只含有小写字母。

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true


"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom_dict = {}
        magazione_dict = {}
        for i in ransomNote:
            if i not in ransom_dict:
                ransom_dict[i] = 0
            ransom_dict[i] += 1
        for i in magazine:
            if i not in magazione_dict:
                magazione_dict[i] = 0
            magazione_dict[i] += 1
        
        for k in ransom_dict:
            if k not in magazione_dict:
                return False
            if magazione_dict[k] < ransom_dict[k]:
                return False
        
        return True
    
    
s = Solution()
ransomNote = "aa"
magazine = "ab"
print s.canConstruct(ransomNote, magazine)