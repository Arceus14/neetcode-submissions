class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row = 0
        for i in range(len(matrix)):
            print(matrix[i])
            if matrix[i][0] <= target <= matrix[i][len(matrix[i]) - 1]:
                row = matrix[i]
                if target in row:
                    return True
        return False
        