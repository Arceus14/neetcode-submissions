class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hmap = {}

        for i, n in enumerate(numbers):
            if n in hmap:
                return [hmap[n] + 1, i + 1]
            hmap[target - n] = i 