class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        lst = []
        for c in s:
            if c.isalnum():
                lst.append(c.lower())
        l = len(lst)
        
        left, right = 0, l - 1
        while left < right:
            if lst[left] != lst[right]:
                return False
            left += 1
            right -= 1
        return True
            