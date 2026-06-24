class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        h = len(numbers) - 1
        while True:
            sum = numbers[l] + numbers[h]
            if sum == target:
                return [l+1, h+1]
            elif sum > target:
                h -= 1
            else:
                l += 1
        