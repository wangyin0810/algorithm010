# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 09:45:25 2020

@author: wangyin
"""
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def dfs(cur, left, right):
            if left == n and right == n:
                res.append(cur)
            if left > right:
                dfs(cur + ")", left, right+1)
            if left < n:
                dfs(cur + "(", left + 1, right)
        dfs("", 0, 0)
        return res