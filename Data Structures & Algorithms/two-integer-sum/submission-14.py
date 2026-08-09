class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        # a + b = target
        # b = target - a
        for i, n in enumerate(nums):
            if n in pairs:
                return [pairs[n], i]
            else:
                pairs[target - n] = i