class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for i in range(len(nums)):
            if nums[i] in hmap:
                return [hmap[nums[i]], i]
            diff = target - nums[i]
            hmap[diff] = i