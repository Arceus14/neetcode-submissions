import string
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        import string
        if len(s1) > len(s2):
            return False
        matches = 0
        a_count = {
            _:0 for _ in list(string.ascii_lowercase)
        }
        s1_count = a_count | dict(Counter(s1))
        s2_count = a_count

        l = 0
        r = len(s1) - 1

        while r < len(s2):
            if l == 0:
                for i in range(len(s1)):
                    s2_count[s2[i]] += 1
                for c1, _ in zip(s1_count, s2_count):
                    if s1_count[c1] == s2_count[c1]:
                        matches += 1
            if matches == 26:
                return True
            
            s2_count[s2[l]] -= 1
            if s2_count[s2[l]] == s1_count[s2[l]]:
                matches += 1
            elif s2_count[s2[l]] + 1 == s1_count[s2[l]]:
                matches -= 1
            l += 1
            r += 1
            if r < len(s2):
                s2_count[s2[r]] += 1
                if s2_count[s2[r]] == s1_count[s2[r]]:
                    matches += 1
                elif s2_count[s2[r]] - 1 == s1_count[s2[r]]:
                    matches -= 1
        return False
                