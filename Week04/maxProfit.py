# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 14:52:24 2020

@author: wangyin
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_value = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                max_value += prices[i] - prices[i-1]
        return max_value