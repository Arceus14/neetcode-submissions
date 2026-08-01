class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        islands = 0
        q = collections.deque()
        maxArea = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            area = 1
            visited.add((r, c))
            q.append((r, c))

            while q:
                x, y = q.pop()
                nbs = [[0, 1],[0, -1], [1, 0], [-1, 0]]

                for xi, yi in nbs:
                    nx, ny = x + xi, y + yi
                    if 0 <= nx < rows and 0 <= ny < cols \
                    and (nx, ny) not in visited \
                    and grid[nx][ny] == 1:
                        visited.add((nx, ny))
                        area += 1
                        q.append((nx, ny))
            return area

        if not grid:
            return 0
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited \
                and grid[r][c] == 1:
                    islands += 1
                    area = bfs(r, c)
                    maxArea = max(maxArea, area)
        return maxArea