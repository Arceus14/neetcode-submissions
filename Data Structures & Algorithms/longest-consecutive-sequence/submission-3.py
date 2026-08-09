class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        hset = set(nums)

        for i in nums:
            length = 0
            if i - 1 not in hset: # Start of a sequence found
                while i + length in hset:
                    length += 1
            longest = max(longest, length)
        return longest
