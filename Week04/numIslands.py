# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 14:52:24 2020

@author: wangyin
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        h = len(grid)
        l = len(grid[0])
        count = 0

        def dfs(grid, i, j):
            if  not 0 <= i < h or not 0 <= j < l or grid[i][j] == '0':
                return 
            grid[i][j] = '0'
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)

        for i in range(h):
            for j in range(l):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1
        return count