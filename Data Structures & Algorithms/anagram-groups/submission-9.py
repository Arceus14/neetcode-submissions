import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hlist = collections.defaultdict(list)
        # single word

        for w in strs:
            hmap = {}
            for c in w:
                hmap[c] = 1 + hmap.get(c, 0)

            hlist[tuple(sorted(list(hmap.items())))].append(w)

        return list(hlist.values())
