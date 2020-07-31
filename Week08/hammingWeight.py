# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 20:44:36 2020

@author: YinWang
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n != 0:
            count += n&1
            n = n>>1
        return count