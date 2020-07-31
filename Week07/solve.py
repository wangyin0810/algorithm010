# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 09:45:25 2020

@author: wangyin
"""

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return []
        m, n = len(board), len(board[0])
        def dfs(board, i, j):
            if 0 <= i < m and 0 <= j < n and board[i][j] == "O":
                board[i][j] = "E"
            else:
                return 
            dfs(board, i+1, j)
            dfs(board, i-1, j)
            dfs(board, i, j-1)
            dfs(board, i, j+1)
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    dfs(board, i, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "E":
                    board[i][j] = "O"
        return board