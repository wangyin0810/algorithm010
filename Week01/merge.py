# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 09:45:25 2020

@author: wangyin
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()