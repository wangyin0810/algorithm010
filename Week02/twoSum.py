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
        hash_map = {}
        for i in range(len(nums)):
            a = target - nums[i]
            if a in hash_map:
                return [i, hash_map[a]]
            else:
                hash_map[nums[i]] = i