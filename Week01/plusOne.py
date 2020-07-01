# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 09:45:25 2020

@author: wangyin
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num =0
        for i in range(len(digits)):
            num = num + digits[i]*10**(len(digits)-i-1)
        return [int(i) for i in str(num+1)]