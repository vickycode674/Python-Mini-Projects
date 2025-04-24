#single number 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        for key, value in d.items():
            if value == 1:
                return key
        return -1
    

    import math
class Solution:
    def isHappy(self, n: int) -> bool:
        attempts = 0  # count the number of attempts

        while True:
            sum=0
            temp=n

            while temp>0:
                digits=temp%10
                sum=sum+digits*digits
                temp=temp//10
        
            if sum == 1:
                return True
             
            attempts+=1
            if attempts > 6:
                return False 
            n=sum

import math
class Solution:
    def isHappy(self, n: int) -> bool:
       seen =set()

       while n!=1:
        if n in seen:
            return False #loop cycle repeated
        
        seen.add(n)
        sum=0

        while n>0:
            digits=n%10
            sum=sum+digits*digits
            n=n//10
        
        n=sum
       return True
    

