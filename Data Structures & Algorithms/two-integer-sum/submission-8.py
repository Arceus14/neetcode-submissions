class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        l = len(nums)
        for i in range(l):
           
            if (target - nums[i]) in hmap:
                return sorted(list([i, hmap[target - nums[i]]]))
            else:
                hmap[nums[i]] = i
