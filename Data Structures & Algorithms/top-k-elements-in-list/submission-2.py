class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = collections.defaultdict(int)

        for n in nums:
            freq[n] += 1
        lst = sorted(freq, key= lambda k : freq[k], reverse=True)   
        return lst[:k]