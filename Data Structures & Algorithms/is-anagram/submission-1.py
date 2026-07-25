class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap1 = collections.Counter(s)
        hmap2 = collections.Counter(t)

        if hmap1 == hmap2:
            return True
        else:
            return False