# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 20:44:36 2020

@author: YinWang
"""

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.count = 0
        def isvalid(row, col, seat):
            if not seat: return True
            for x, y in seat:
                if col == y or row+col == x+y or row-col == x-y:
                    return False
            return True
        def dfs(row, seat):
            if row == n:
                self.count += 1
                return 
            for col in range(n):
                if isvalid(row, col, seat):
                    dfs(row+1, seat+[(row, col)])
        dfs(0, [])
        return self.count
