#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 19:07:13 2018

@author: zhoujw
"""

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        dic1,dic2={},{}
        
        for index,value in enumerate(nums1):
            dic1[value]=dic1.get(value,0)+1
        for index,value in enumerate(nums2):
            dic2[value]=dic2.get(value,0)+1
        
        res = []
        for i in dic1:
            if i in dic2:
                res = res+[i]*min(dic1[i],dic2[i])
        
        return res


nums1 = [1,2,2,1]
nums2 = [2,2]

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(Solution().intersect(nums1,nums2))

"""
这道题用python库collections里面有Counter!!
"""

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        from collections import Counter
        
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        r = list((c1&c2).elements())
        return r
    
nums1 = [1,2,2,1]
nums2 = [2,2]
print(Solution().intersect(nums1,nums2))
        
        