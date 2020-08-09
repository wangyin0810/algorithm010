# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 20:44:36 2020

@author: YinWang
"""

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = ""
        l = len(s)
        index = 0
        while index < l//k:
            if index%2 == 0:
                res += s[k*index:k*(index+1)][::-1]
            else:
                res += s[k*index:k*(index+1)]
            index += 1
        if (l//k)%2 == 0 and l%k != 0:
            res += s[index*k:][::-1]
        if (l//k)%2 == 1 and l%k != 0:
            res += s[index*k:]
        return res