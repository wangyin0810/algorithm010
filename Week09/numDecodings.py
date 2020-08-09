# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 20:44:36 2020

@author: YinWang
"""

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l =len(s)
        if not s: return 0
        if s[0] == "0": return 0
        dp = [1]*(l+1)
        for i in range(1, l):
            if s[i] == "0":
                if s[i-1] == "1" or s[i-1] == "2":
                    dp[i+1] = dp[i-1]
                else:
                    return 0
            else:
                dp[i+1] = dp[i]
                if 10 < int(s[i-1:i+1]) <= 26:
                    dp[i+1] += dp[i-1]
        return dp[-1]