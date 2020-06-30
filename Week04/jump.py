# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 14:52:24 2020

@author: wangyin
"""

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2: return 0 
        if nums[0] >= len(nums)-1: return 1 
        cur = 0
        step = 1
        max_to = nums[0]
        while max_to < len(nums)-1:
            step += 1 
            for i in range(cur+1, max_to+1):
                if nums[i] + i > max_to:
                    max_to = nums[i] + i
                    cur = i
                if max_to >= len(nums) - 1:
                    return step
            
        return step