# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 20:44:36 2020

@author: YinWang
"""

class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        res = ""
        s = ""
        for i in S:
            if 65 <= ord(i) <= 90 or 97 <= ord(i)<= 122:
                s += i
        s = s[::-1]
        index = 0
        for i in range(len(S)):
            if 65 <= ord(S[i]) <= 90 or 97 <= ord(S[i]) <= 122:
                res += s[index]
                index += 1
            else:
                res += S[i]
        return res