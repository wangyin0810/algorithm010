# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 09:45:25 2020

@author: wangyin
"""

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        rec = []
        def backtrack(start, cur):
            if len(cur) == k:
                rec.append(cur[:])
            for i in range(start, n+1):
                cur.append(i)
                backtrack(i+1, cur)
                cur.pop()
        backtrack(1,[])
        return rec