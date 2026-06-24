class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # a + b = target
        # => b = target - a

        hmap = {}
        for a in nums:
            b = target - a
            if a in hmap or b in hmap:
                if a == b:
                    return sorted([nums.index(a), nums.index(b, nums.index(a)+1)])
                return sorted([nums.index(a), nums.index(b)])
            else:
                hmap[b] = a