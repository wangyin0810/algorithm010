# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 14:52:24 2020

@author: wangyin
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)-1
        if left == right:
            if nums[left] == target:
                return left
            else:
                return -1
        while right >= left :
            mid = (left + right)//2
            if nums[mid] == target: return mid
            if nums[mid] > nums[left]:  #mid在有序部分
                if nums[left] < target < nums[mid]:
                    right = mid - 1
                elif nums[left] == target:
                    return left
                else:
                    left = mid + 1
            else:   
                if nums[mid] < target < nums[right]:
                    left = mid +1
                elif nums[right] == target:
                    return right
                else:
                    right = mid - 1
        return -1