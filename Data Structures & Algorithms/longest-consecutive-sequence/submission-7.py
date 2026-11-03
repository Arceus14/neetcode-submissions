class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums = sorted(list(set(nums)))
        nums = set(nums)
        l = len(nums)
        if l == 0 or l == 1:
            return l
        maxLen = 1
        for n in nums:
            count = 0
            if n - 1 not in nums:
                while n in nums:
                    count += 1
                    n += 1
                maxLen = max(maxLen, count)
        return maxLen    