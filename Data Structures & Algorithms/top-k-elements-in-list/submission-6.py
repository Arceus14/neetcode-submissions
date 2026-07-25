class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = dict(collections.Counter(nums))

        return sorted(freq, key=lambda x: freq[x], reverse=True)[:k]

