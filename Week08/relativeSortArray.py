# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 20:44:36 2020

@author: YinWang
"""

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        hashmap = {}
        res = []
        end = []
        arr2 = arr2
        for i in arr1:
            if i in arr2:
                if i in hashmap:
                    hashmap[i] += 1
                else:
                    hashmap[i] = 1
            else:
                end.append(i)
        for i in arr2:
            for j in range(hashmap[i]):
                res.append(i)
        end.sort()
        return res+end
