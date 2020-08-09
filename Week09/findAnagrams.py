# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 20:44:36 2020

@author: YinWang
"""

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        p_hash = [0]*123
        s_hash = [0]*123
        for i in p:
            p_hash[ord(i)] += 1
        for j in s[:len(p)]:
            s_hash[ord(j)] += 1
        
        if p_hash == s_hash:
            res.append(0)
        for i in range(1, len(s)-len(p)+1):
            s_hash[ord(s[i+len(p)-1])] += 1
            s_hash[ord(s[i-1])] -= 1
            if s_hash == p_hash:
                res.append(i)
        return res