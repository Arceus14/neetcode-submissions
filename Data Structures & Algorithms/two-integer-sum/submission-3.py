class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        l = len(nums)
        for i in range(l):
            rem = target - nums[i]
            if rem in hmap:
                return sorted(list([i, hmap[rem]]))
            else:
                hmap[nums[i]] = i
