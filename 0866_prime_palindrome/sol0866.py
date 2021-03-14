'''
Created on Mar 14, 2021

@author: Q
'''
class Solution(object):
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        def is_prime(n):
            if n<2: return False
            for i in range(2,n//2):
                if n % i==0:
                    return False
            return True
        
        def is_Palindrome(n):
            str_n = str(n)
            len_n = len(str_n)
            for i in range(len_n//2):
                if str_n[i]!=str_n[len_n-1-i]:
                    return False
            return True
        
        while True:
            if is_Palindrome(N) and is_prime(N):
                    return N
            N+=1
            
N = 4
msol = Solution()
ares = msol.primePalindrome(N)
print(ares)     
                    
    