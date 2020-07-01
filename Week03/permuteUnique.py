# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 09:45:25 2020

@author: wangyin
"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rec = []
        nums.sort()
        def backtrace(nums, cur):
            if not nums:
                rec.append(cur)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                backtrace(nums[:i]+nums[i+1:],cur + [nums[i]])
            return rec
        backtrace(nums, [])
        return rec