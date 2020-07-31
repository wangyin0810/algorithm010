# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 20:44:36 2020

@author: YinWang
"""

class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.pre = None
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = ListNode(None)
        self.end = ListNode(None)
        self.head.next = self.end
        self.end.pre = self.head

        self.hashmap = {}


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hashmap:
            node = self.hashmap[key]
            self.move_node_2_end(node)
            return node.value
        else:
            return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.hashmap:
            node = self.hashmap[key]
            node.value = value
            self.move_node_2_end(node)
        else:
            if len(self.hashmap) == self.capacity:
                self.hashmap.pop(self.head.next.key)
                self.head.next = self.head.next.next
                self.head.next.pre = self.head
            new = ListNode(key)
            self.hashmap[key] = new
            self.hashmap[key].value = value
            new.next = self.end
            new.pre = self.end.pre
            self.end.pre.next = new
            self.end.pre = new

    def move_node_2_end(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        node.next = self.end
        node.pre = self.end.pre
        self.end.pre.next = node
        self.end.pre = node