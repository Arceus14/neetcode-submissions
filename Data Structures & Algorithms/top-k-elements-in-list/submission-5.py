class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = dict(collections.Counter(nums))

        lst = sorted(freq, key=lambda x: freq[x], reverse=True)
        return lst[:k]

