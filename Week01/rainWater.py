# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 09:45:25 2020

@author: wangyin
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        ans = 0
        i = 0
        while i < len(height):

            while stack and height[i]  > height[stack[-1]]:
                a = stack.pop()
                if stack == []: break
                h = min(height[i],height[stack[-1]]) - height[a]
                l = i - stack[-1] - 1
                ans += h * l
            stack.append(i)
            i += 1
        return ans