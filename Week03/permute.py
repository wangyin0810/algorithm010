# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 09:45:25 2020

@author: wangyin
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rec = []
        def backtrack(nums, tmp):
            if not nums:
                rec.append(tmp)
            for i in range(len(nums)):
                backtrack(nums[:i]+nums[i+1:], tmp+[nums[i]])
            return rec
        backtrack(nums, [])
        return rec