class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)

        for word in strs:
            freq = [0 for i in range(26)]
            for l in word:
                ascii = ord(l) - ord('a')
                freq[ascii] += 1
            freq = tuple(freq.copy())
            groups[freq].append(word)
        
        res = []
        for v in groups.values():
            res.append(v)

        return res