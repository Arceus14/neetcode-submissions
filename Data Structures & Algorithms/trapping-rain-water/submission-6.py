class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        l, r = 0, len(height)-1
        leftMax = height[l]
        rightMax = height[r]
        res = 0


        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax-height[l]

            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax-height[r]
        return res

















        # size = len(height)
        # max_left = [0] * size
        # max_right = [0] * size
        # min_lr = [0] * size

        # for i in range(1, size):
        #     max_left[i] = max(max_left[i-1], height[i-1])
        #     max_right[size-1-i] = max(max_right[size-i], height[size-i])
        # vol = 0
        
        # for i in range(size):
        #     min_lr[i] = min(max_left[i], max_right[i])
        #     if min_lr[i] - height[i] >= 0:
        #         vol += min_lr[i] - height[i]
        # return vol
















