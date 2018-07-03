#-*- coding: utf-8 -*-

"""

https://leetcode-cn.com/problems/goat-latin/description/

给定一个由空格分割单词的句子 S。每个单词只包含大写或小写字母。

我们要将句子转换为 “Goat Latin”（一种类似于 猪拉丁文 - Pig Latin 的虚构语言）。

山羊拉丁文的规则如下：

如果单词以元音开头（a, e, i, o, u），在单词后添加"ma"。
例如，单词"apple"变为"applema"。

如果单词以辅音字母开头（即非元音字母），移除第一个字符并将它放到末尾，之后再添加"ma"。
例如，单词"goat"变为"oatgma"。

根据单词在句子中的索引，在单词最后添加与索引相同数量的字母'a'，索引从1开始。
例如，在第一个单词后添加"a"，在第二个单词后添加"aa"，以此类推。
返回将 S 转换为山羊拉丁文后的句子。

"""

import string

class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        alpha_dict = {}
        for i in string.lowercase:
            alpha_dict[i] = 1
        yuanyin = ["a", "e", "i", "o", "u"]
        
        word = ""
        index = 0
        result = ""
        for w in S:
            if w.lower() not in alpha_dict:
                if word:
                    if word[0].lower() in yuanyin:
                        result += word
                    else:
                        result += word[1:] + word[0]
                    index += 1
                    result += "ma" + "a"*index + " "
                    word = ""
                continue
            word += w 
        
        if word:
            if word[0].lower() in yuanyin:
                result += word 
            else:
                result += word[1:] + word[0]
            index += 1
            result += "ma" + "a"*index
        result = result.strip()
        return result
            
                    
                    
        

        
    
s = Solution()
S = "I speak Goat Latin"
result =  s.toGoatLatin(S)
print result
print "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
print "Imaa peaksmaaa oatGmaaaa atinLmaaaaa" == result
S = "The quick brown fox jumped over the lazy dog"
S = "Each word consists of lowercase and uppercase letters only"
result =  s.toGoatLatin(S)
print result

