class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)
        maxLeft = [0] * size
        maxRight = [0] * size

        ml = 0
        for i, n in enumerate(height):
            maxLeft[i] = ml
            ml = max(n, ml)
        mr = 0
        for i, n in enumerate(reversed(height)):
            maxRight[size - 1 - i] = mr
            mr = max(n, mr)
        rainArea = 0
        for i, n in enumerate(height):
            area = min(maxLeft[i], maxRight[i]) - n
            area = max(area, 0)
            rainArea += area
        return rainArea