# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 20:44:36 2020

@author: YinWang
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap = {}
        m = set()
        l = len(s)
        if len(s) != len(t): return False
        for i in range(l):
            if s[i] in hashmap:
                if hashmap[s[i]] != t[i]:
                    return False
            else:
                if t[i] in m:
                    return False
                else:
                    hashmap[s[i]] = t[i]
                    m.add(t[i])
        return True