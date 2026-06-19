class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
                
        l = len(nums)
        op = [1 for i in range(l)]


        # Adding prefixes:
        prefix = 1
        for i in range(l):
            op[i] = prefix
            prefix *= nums[i]
        # Adding postfixes:
        postfix = 1
        for i in reversed(range(l)):
            op[i] *= postfix
            postfix *= nums[i]

        return op