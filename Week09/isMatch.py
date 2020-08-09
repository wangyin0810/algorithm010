# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 20:44:36 2020

@author: YinWang
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_l, p_l = len(s), len(p)
        dp = [[False]*(s_l+1) for _ in range(p_l+1)]
        dp[0][0] = True
        for k in range(1, p_l+1):
            if p[k-1] == "*":
                dp[k][0] = dp[k-1][0]
        for i in range(1, p_l+1):
            path = False
            for j in range(1, s_l+1):
                if p[i-1] == "*":
                    if dp[i-1][0]:
                        dp[i] = [True]*(s_l+1)
                    if dp[i-1][j]:
                        path = True
                    if path:
                        dp[i][j] = True
                elif p[i-1] == "?":
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1]
        return dp[-1][-1]