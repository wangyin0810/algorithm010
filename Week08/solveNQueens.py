# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 20:44:36 2020

@author: YinWang
"""

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        
        res = []
        def transfer(seat):
            grid = [["." for i in range(n)] for i in range(n)]
            for x, y in seat:
                grid[x][y] = "Q"

            return ["".join(grid[i]) for i in range(n)]

        def isvalid( row, col, seat):
            if not seat: return True
            for x, y in seat:
                if col == y or row+col == x+y or row-col == x-y:
                    return False
            return True
        def dfs( row, seat):
            if row == n:
                res.append(transfer(seat))
                return 
            for col in range(n):
                if isvalid(row, col, seat):
                    dfs(row+1, seat+[(row, col)])
        dfs(0, [])
        return res
