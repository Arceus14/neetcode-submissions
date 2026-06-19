class Solution:
    def isHappy(self, n: int) -> bool:
        sum = 0
        check = set()
        while True:
            sum = 0
            while n > 0:
                sum += (n % 10)**2
                n //= 10
            if sum == 1:
                return True
                exit()
            else:
                n = sum
                
                if sum in check:
                    return False
                    exit()
                else:
                    check.add(sum)

             
        
        
