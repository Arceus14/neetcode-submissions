class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a_index = 0
        b_index = 0
        for a in range(len(numbers)):
            b = target - numbers[a]
            if numbers[a] == b:
                return [a+1, a+2]
            # Binary search for index of 'b'
            low = a
            high = len(numbers) - 1
            while(low <= high):
                mid = (low+high)//2
                if numbers[mid] == b:
                    b_index = mid + 1
                    a_index = a + 1
                    return sorted([a_index, b_index])
                elif numbers[mid] < b:
                    low = mid + 1
                else:
                    high = mid -1