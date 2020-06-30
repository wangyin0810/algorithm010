# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 14:52:24 2020

@author: wangyin
"""

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i, j, k = 0, 0, 0
        while i <= len(g)-1 and j <= len(s)-1:
            if s[j] >= g[i]:
                k += 1
                i += 1
                j += 1
            else:
                j += 1
        return k