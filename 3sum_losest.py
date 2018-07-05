#-*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/3sum-closest/description/

给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2)

"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nlen = len(nums)
        result = nums[0] + nums[1] + nums[2]
        min_diff = abs(result- target)
        nums.sort()
        for i in xrange(nlen):
            left = i + 1 
            right = nlen - 1
            while left < right:
                sums = nums[i] + nums[left] + nums[right]
                diff = abs(sums - target)
                if diff == 0:
                    return sums 
                if diff < min_diff:
                    result = sums
                    min_diff = diff
                if sums < target:
                    left += 1
                else:
                    right -= 1
        
        return result
                

s = Solution()
nums = [-1, 2, 1, -4]
target = 1
print s.threeSumClosest(nums, target)
    
    