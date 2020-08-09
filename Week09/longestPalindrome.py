# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 20:44:36 2020

@author: YinWang
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2: return s
        res = ""
        for i in range(len(s)):
            s1 = self.expand(i, i, s)
            s2 = self.expand(i, i+1, s) 
            if len(s1) >= len(s2):
                S = s1
            else:
                S = s2
            if len(S) > len(res):
                res = S
        return res

    def expand(self, left, right, s):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]