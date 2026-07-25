class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # a + b = target
        # => b = target - a

        hmap = {}
        for i, n in enumerate(nums):
            if n in hmap:
                return [hmap[n], i]
            else:
                hmap[target-n] = i
