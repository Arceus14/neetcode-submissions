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

        res = []
        for v in hlist.values():
            res.append(v)
        return res
