# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 09:45:25 2020

@author: wangyin
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hash_map = {}
        if len(s) != len(t): return False
        for i in s:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1
        for j in t:
            if j in hash_map:
                hash_map[j] -= 1
            else:
                hash_map[j] = 1
        for k in hash_map:
            if hash_map[k] != 0:
                return False
        return True