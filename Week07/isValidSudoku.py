# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 09:45:25 2020

@author: wangyin
"""
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        blank = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    b = (i//3 )*3 + j//3 
                    if board[i][j] in row[i]:
                        return False
                    else:
                        row[i].add(board[i][j])
                    if board[i][j] in col[j]:
                        return False
                    else:
                        col[j].add(board[i][j])
                    if board[i][j] in blank[b]:
                        return False
                    else:
                        blank[b].add(board[i][j])
        return True
        

