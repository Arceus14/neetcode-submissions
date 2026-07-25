class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        lst = []
        for c in s:
            if c.isalnum():
                lst.append(c.lower())
        l = len(lst)
        
        if l % 2 == 0:
            if lst[:l//2] == lst[:l//2 - 1: -1]:
                return True
        else:
            if lst[:l//2] == lst[:l//2 : -1]:
                return True
        return False