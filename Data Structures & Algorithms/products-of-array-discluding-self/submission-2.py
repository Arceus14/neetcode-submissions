class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
         
        res = []
         
        # pre multipliers:
        prod = 1
        for n in nums:
            res.append(prod)
            prod *= n
        prod = 1
        size = len(nums) - 1

        # post multipliers:
        for i, n in enumerate(reversed(nums)):
            res[size - i] *= prod
            prod *= n
        return res
