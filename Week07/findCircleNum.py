# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 09:45:25 2020

@author: wangyin
"""

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        count = 0
        n = len(M)
        visited = set()
        def dfs(i):
            for j in range(n):
                if M[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)
                              
        for i in range(n):
            if i not in visited:
                count += 1
                visited.add(i)
                dfs(i)
            
        return count