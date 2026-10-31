class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        prod = 1
        for i, n in enumerate(nums):
            pre.append(prod)
            prod *= n
        
        l = len(nums)
        post = [0]*l
        post[l-1] = 1
        prod = 1
        for i, n in enumerate(nums):
            post[l-1-i] = prod
            prod *= nums[l-1-i]
        
        fin = [0]*l
        for i, n in enumerate(nums):
            fin[i] = (pre[i]*post[i])
        return fin       