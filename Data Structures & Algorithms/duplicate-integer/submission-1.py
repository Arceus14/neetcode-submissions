class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #flag = False
        check = []
        for u in nums:
            if u in check:
                return True
            check.append(u)
        return False
            #for j in range(nums[u+1],):
