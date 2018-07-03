#-*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/3sum/description/

给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        result_dict = {}
        filter_dict = {}
        new_nums = []
        for num in nums:
            if filter_dict.setdefault(num, 0)>2:
                continue
            filter_dict[num] += 1
            new_nums.append(num) 
        
        nlen = len(new_nums)
        nums_dict = {}
        new_nums.sort()
        for num in new_nums:
            nums_dict.setdefault(num, 0)
            nums_dict[num] += 1
        for i in xrange(nlen):
            if new_nums[i] > 0:
                break
            for j in xrange(i+1, nlen):
                remain = -new_nums[i]-new_nums[j]
                if remain not in nums_dict:
                    continue
                t = {}
                t[new_nums[i]] = nums_dict[new_nums[i]]
                t[new_nums[j]] = nums_dict[new_nums[j]]
                t[remain] = nums_dict[remain]
                t[new_nums[i]] -= 1
                t[new_nums[j]] -= 1
                t[remain] -= 1
                for k in t:
                    if t[k] < 0:
                        break
                else:
                    v = [new_nums[i], new_nums[j], remain]
                    v.sort()
                    if str(v) not in result_dict:
                        result_dict[str(v)] = 1
                        result.append(v)
        
        return result
                    
 

s = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print s.threeSum(nums)








