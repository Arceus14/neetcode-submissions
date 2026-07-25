from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}

        for w in strs:
            count = [0] * 26

            for c in w:
                count[ord(c) - ord('a')] += 1
            count = tuple(count)
            if count in hmap:
                hmap[count].append(w)
            else:
                hmap[count] = [w]
        return list(hmap.values())