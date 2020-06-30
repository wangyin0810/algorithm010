# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 14:52:24 2020

@author: wangyin
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """ 
        m = len(matrix)
        if m == 0: return False
        n = len(matrix[0])
        left, right = 0, m*n-1
        while left <= right:
            mid = (left + right)//2
            mid_val = matrix[mid//n][mid%n]
            if mid_val == target:
                return True
            elif mid_val > target:
                right = mid - 1 
            else:
                left = mid + 1 
        return False