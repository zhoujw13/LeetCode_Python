#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 19:02:26 2018

@author: zhoujw
"""

class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        res =list( set(nums1) & set(nums2))
        
        return res
    
"""
这个题应该是相当简单了，用集合求交集即可
"""