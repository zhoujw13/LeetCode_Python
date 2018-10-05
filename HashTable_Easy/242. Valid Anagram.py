#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 18:22:15 2018

@author: zhoujw
"""

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        dic1= {}
        dic2 ={}#这里一定不能写dci1=doc2={}这样的话两个dic一直是同一个！！！
        for i in s:
            dic1[i] = dic1.get(i,0)+1
        for j in t:
            dic2[j] = dic2.get(j,0)+1
        
        if dic1==dic2:
            return True
        return False
    
s = "anagram"
t = "nagaram"

s = "rat"
t = "caar"
print(Solution().isAnagram(s,t))

