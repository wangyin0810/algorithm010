# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 20:44:36 2020

@author: YinWang
"""

class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.count = 0

        def mergesort(nums):
            l = len(nums)
            if l < 2:
                return nums
            left = nums[:l//2]
            right = nums[l/2:]
            return merge(mergesort(left), mergesort(right))
        def merge(left, right):
            l, r = 0, 0
            while l < len(left) and r < len(right):
                if left[l] > 2*right[r]:
                    self.count += len(left) - l
                    r += 1
                else:
                    l += 1
            return sorted(left + right)
        mergesort(nums)
        return self.count
