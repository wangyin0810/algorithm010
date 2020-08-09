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
        s = s.strip()
        res = []
        cur = ""
        for i in s:
            if i != " ":
                cur += i
            else:
                if cur:
                    res = [cur] + res
                cur = ""
        if cur:
            res = [cur]+ res
        return " ".join(res)