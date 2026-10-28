import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        h1 = collections.Counter(s)
        h2 = collections.Counter(t)

        if h1 == h2:
            return True
        return False