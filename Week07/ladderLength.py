# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 09:45:25 2020

@author: wangyin
"""
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        count = 1
        queue = []
        queue.append(beginWord)
        visited = set()
        wordList = set(wordList)
        while queue:
            k = len(queue)
            for _ in range(k):
                cur = queue.pop(0)
                if cur == endWord:
                    return count 
                for i in range(len(cur)):
                    for j in "abcdefghijklmnopqrstuvwxyz":
                        tmp = cur[:i] + j + cur[i+1:]
                        if tmp in wordList and tmp not in visited:
                            queue.append(tmp)
                            visited.add(tmp)
            count += 1
        return 0