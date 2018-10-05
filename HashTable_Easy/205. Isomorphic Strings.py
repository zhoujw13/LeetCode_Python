#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 10:24:48 2018

@author: zhoujw
"""

class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        dic ={}
        for a in zip(s,t):
            if dic.get(a[1],a[0])==a[0]:
                dic[a[1]]=a[0]
                continue
            else:
                return False
            
        return True

#s = "paper"
#t = "title"
#s = "foo"
#t = "bar"
s="ab"
t="aa"
print(Solution().isIsomorphic(s,t))

"""
注意一下几点：
1、字母可以Map自己
2、字典初始化问题  get是一个好用的函数！
3、究竟是谁map谁，一定要弄明白哪一个是key哪一个是value
还是不对！！

"""

"""
有一种一一对应关系！！！用集合里元素数量！！！
"""

class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        return bool(len(set(s))==len(set(t))==len(set(zip(s,t))))

"""
现在明白了，这是一个双向的关系，一一对应的，所以单向的比较是不对的
“”“