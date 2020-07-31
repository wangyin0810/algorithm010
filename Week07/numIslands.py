# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 09:45:25 2020

@author: wangyin
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        def recur(grid, i, j):
            if len(grid) > i >= 0 and len(grid[0]) > j >= 0 and grid[i][j] == "1":
                grid[i][j] = "0"
            else:
                return 
            recur(grid, i+1, j)
            recur(grid, i-1, j)
            recur(grid, i, j+1)
            recur(grid, i, j-1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    recur(grid, i, j)
                    count += 1
        return count