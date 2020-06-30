# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 14:52:24 2020

@author: wangyin
"""

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        dic = {5:0, 10:0, 20:0}
        for i in bills:
            if i == 5:
                dic[5] += 1
            elif i == 10:
                if dic[5] > 0:
                    dic[5] -= 1
                    dic[10] += 1
                else:
                    return False
            else:
                if dic[10] > 0 and dic[5] > 0:
                    dic[10] -= 1
                    dic[5] -= 1
                    dic[20] += 1
                elif dic[10] == 0 and dic[5] >= 3:
                    dic[5] -= 3
                    dic[20] += 1
                else:
                    return False
        return True