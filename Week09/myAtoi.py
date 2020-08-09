# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 20:44:36 2020

@author: YinWang
"""

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        syb = {"+", "-"}
        s = str.strip()
        res = ""
        if not s:
            return 0
        if s[0] in syb or s[0] in "123467890":
            res += s[0]
        else:
            return 0
        for i in range(1, len(s)):
            if s[i] in "1234567890":
                res += s[i]
            else:
                break
        if res in syb: return 0
        return min(2**31-1, int(res)) if int(res) > 0 else max(int(res), -2**31)