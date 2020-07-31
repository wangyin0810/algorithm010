# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 09:45:25 2020

@author: wangyin
"""
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        def isvalid(x, y, seat):
            if not seat: return True
            for m, n in seat:
                if y == n or y-x == n-m or x+y == m+n:
                    return False
            return True
        def dfs(row, seat):
            if row == n:
                res.append(seat)
                return 
            
            for col in range(n):
                if isvalid(row, col, seat):
                    dfs(row + 1, seat + [(row, col)])
        dfs(0, [])
        
        output = []
        for ans in res:
            M = [["." for i in range(n)] for i in range(n)]
            for x, y in ans:
                M[x][y] = "Q"
            output.append(M)
        return [["".join(i) for i in j] for j in output]