class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)
        max_left = [0] * size
        max_right = [0] * size
        min_lr = [0] * size

        for i in range(1, size):
            max_left[i] = max(max_left[i-1], height[i-1])
            max_right[size-1-i] = max(max_right[size-i], height[size-i])
        
        vol = 0
        
        for i in range(size):
            min_lr[i] = min(max_left[i], max_right[i])

            if min_lr[i] - height[i] >= 0:
                vol += min_lr[i] - height[i]
        return vol

