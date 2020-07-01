# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 09:45:25 2020

@author: wangyin
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            if target - nums[i] not in dic:
                dic[nums[i]] = i
            else:
                return [dic[target-nums[i]],i]