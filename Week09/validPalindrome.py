# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 20:44:36 2020

@author: YinWang
"""

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == s[::-1]: return True
        left, right = 0, len(s)-1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                if s[left+1:right+1] == s[left+1:right+1][::-1]:
                    return True
                elif s[left:right] == s[left:right][::-1]:
                    return True
                else:
                    return False