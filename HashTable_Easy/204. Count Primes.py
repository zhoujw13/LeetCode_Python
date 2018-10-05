# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        """
        这个方法是把[1,n-1]的数列中数字究竟是质数还是合数先判断出来，因为两项乘机必然不是质数
        另外就是：xrange在python3里面取消了，range就死一个迭代器
        没有if res[i]==True的判断还是会超时
        所以还是得加上这个判断
        """
        
        """
        显然以上的枚举法，不管如何改进都是不能AC的，所以枚举法肯定是行不通的。
        用筛法求素数的基本思想是：把从1开始的、某一范围内的正整数从小到大顺序排列， 1不是素数，首先把它筛掉。剩下的数中选择最小的数是素数，然后去掉它的倍数。依次类推，直到筛子为空时结束。如有：1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 
        1不是素数，去掉。剩下的数中2最小，是素数，去掉2的倍数，余下的数是：
        3 5 7 9 11 13 15 17 19 21 23 25 27 29
        剩下的数中3最小，是素数，去掉3的倍数，如此下去直到所有的数都被筛完，求出的素数为：
        2 3 5 7 11 13 17 19 23 29
          """
        
        
        if n==1 or n==2 or n==0:
            return 0
        
        res = [True]*n
        res[0]=False
        res[1]=False
        
        for i in range(2,n):
            if res[i]==True:
                for j in range(2,(n-1)//i+1):
                    res[i*j]=False
        return sum(res)
    
print(Solution().countPrimes(10))