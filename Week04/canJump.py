# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 14:52:24 2020

@author: wangyin
"""

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = len(nums)-2
        cur = len(nums)-1
        while i >= 0:
            if nums[i] + i >= cur:
                cur = i
                i -= 1
            else:
                if i == 0:
                    return False
                i -= 1
        return True