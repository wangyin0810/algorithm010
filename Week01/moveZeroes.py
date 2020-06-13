# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 09:45:25 2020

@author: wangyin
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        m = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[m] = nums[i]
                m += 1
        for k in range(m, len(nums)):
            nums[k] = 0