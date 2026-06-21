from itertools import combinations
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        lst = list()
        for i in range(l):
            target = -1*nums[i]
            hmap = {}
            l = len(nums)
            for j in range(i+1,l):
                if (target - nums[j]) in hmap:
                    ele = sorted(list([-1*target, (target)-nums[j], nums[j]]))
                    if ele not in lst:
                        lst.append(ele)
                else:
                    hmap[nums[j]] = j
        return lst