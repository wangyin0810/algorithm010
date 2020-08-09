# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 20:44:36 2020

@author: YinWang
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        S = s.split()
        res = ""
        for i in range(len(S)):
            S[i] = S[i][::-1]
        return " ".join(S)