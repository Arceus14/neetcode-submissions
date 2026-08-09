class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict(collections.Counter(nums))

        lst = list(counts.keys())
        return sorted(lst, key= lambda x: counts[x], reverse=True)[:k]