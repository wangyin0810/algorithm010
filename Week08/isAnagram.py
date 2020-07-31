# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 20:44:36 2020

@author: YinWang
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap = {}
        if len(s) != len(t): return False
        for i in s:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        for j in t:
            if j in hashmap:
                hashmap[j] -= 1
            else:
                hashmap[j] = 1
        for k in hashmap:
            if hashmap[k] != 0:
                return False
        return True
