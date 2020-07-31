# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 20:44:36 2020

@author: YinWang
"""

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals: return []
        intervals.sort()
        res = []
        res.append(intervals[0])
        k = len(intervals)
        for i in range(1,k):
            x0, x1 = intervals[i][0], intervals[i][1]
            if x0 > res[-1][1]:
                res.append([x0,x1])
            elif x0 <= res[-1][1] < x1:
                res[-1][1] = x1
            elif res[-1][1] >= x1:
                continue
        return res