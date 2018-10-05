#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 18:33:08 2018

@author: zhoujw
"""

class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s = str.split(' ')
        
        return len(set(pattern))==len(set(s))==len(set(zip(s,pattern)))
    
pattern = "abba"
str = "dog dog dog dog"
print(Solution().wordPattern(pattern,str))

"""
上述方法错误，顺序问题很重要
"""

class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        s = str.split(' ')
        n = len(pattern)
        dic1={}
        dic2={}
        
        for i,j in enumerate(s):
            dic1[j]=dic1.get(j,[])+[i]
            
        for i in range(n):
            dic2[pattern[i]]=dic2.get(pattern[i],[])+[i]
        
        return sorted(dic1.values())==sorted(dic2.values())
pattern = "abba"
str = "dog dog dog dog"
print(Solution().wordPattern(pattern,str))