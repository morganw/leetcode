#-*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/compare-version-numbers/description/

比较两个版本号 version1 和 version2。
如果 version1 > version2 返回 1，如果 version1 < version2 返回 -1， 除此之外返回 0。

你可以假设版本字符串非空，并且只包含数字和 . 字符。

 . 字符不代表小数点，而是用于分隔数字序列。

例如，2.5 不是“两个半”，也不是“差一半到三”，而是第二版中的第五个小版本。

示例 1:

输入: version1 = "0.1", version2 = "1.1"
输出: -1
示例 2:

输入: version1 = "1.0.1", version2 = "1"
输出: 1
示例 3:

输入: version1 = "7.5.2.4", version2 = "7.5.3"
输出: -1

"""

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = version1.split(".")
        version2 = version2.split(".")
        version1 = [int(i) for i in version1]
        version2 = [int(i) for i in version2]
        n1 = len(version1)
        n2 = len(version2)
        n = max(n1, n2)
        for i in range(n):
            v1 = version1[i] if len(version1)>i else 0
            v2 = version2[i] if len(version2)>i else 0
            if v1 > v2:
                return 1
            if v1 < v2:
                return -1
            
        return 0
            

    
s = Solution()
version1 = "01"
version2 = "1"
print s.compareVersion(version1, version2)
    
    
    
    
    
    