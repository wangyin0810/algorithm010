# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 14:52:24 2020

@author: wangyin
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return nums[0] 
        left, right = 0, len(nums)-1
        if nums[left] < nums[right]: return nums[0]
        while left < right:
            mid = (left + right)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid 
        return nums[left]