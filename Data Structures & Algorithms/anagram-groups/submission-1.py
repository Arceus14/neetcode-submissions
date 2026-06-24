class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = collections.defaultdict(list)

        for word in strs:
            freq = [0 for i in range(26)]
            for l in word:
                ascii = ord(l) - 97
                freq[ascii] += 1
            freq = tuple(freq)
            anagram[freq].append(word)
        lst = []
        for value in anagram.values():
            lst.append(value)
        return lst