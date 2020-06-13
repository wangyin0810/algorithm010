# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 09:45:25 2020

@author: wangyin
"""

class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.deque = []
        self.k = k
        

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if len(self.deque) < self.k:
            self.deque = self.deque[::-1]
            self.deque.append(value)
            self.deque = self.deque[::-1]
            return True
        else:
            return False
       

        

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if len(self.deque) < self.k:
            self.deque.append(value)
            return True
        else:
            return False
        
        

        

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.deque != []:
            self.deque.pop(0)
            return True
        

        

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.deque != []:
            self.deque.pop()
            return True
        
        

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.deque == []:
            return -1
        else:
            return self.deque[0]
        

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.deque ==[]:
            return -1
        else:
            return self.deque[-1]
        
        

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        if self.deque == []:
            return True
        else:
            return False

        

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        if len(self.deque) == self.k:
            return True
        else:
            return False