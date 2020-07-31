# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 09:45:25 2020

@author: wangyin
"""
class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        queue = []
        queue.append(start)
        dic = {"A":"CGT", "C":"AGT", "G":"ACT", "T":"ACG"}
        count = 0
        visited = set()
        bank = set(bank)
        while queue:
            k = len(queue)
            for _ in range(k):
                node = queue.pop(0)
                if node == end:
                    return count
                for i in range(len(node)):
                    for j in dic[node[i]]:
                        cur = node[:i] + j + node[i+1:]
                        if cur in bank and cur not in visited:
                            queue.append(cur)
                            visited.add(cur)
            count += 1
        return -1