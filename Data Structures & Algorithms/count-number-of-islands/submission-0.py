class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        if not grid:
            return islands

        def bfs(r, c):
            queue = collections.deque()
            queue.append((r, c))
            visited.add((r, c))
            while queue:
                x, y = queue.popleft()
                nbs = [
                    (0, 1), # up
                    (0, -1), # down
                    (1, 0), # right
                    (-1, 0) # left
                ]
                for xi, yi in nbs:
                    nx, ny = x + xi, y + yi
                    if nx in range(rows) and \
                        ny in range(cols) and \
                        grid[nx][ny] == '1' and \
                        (nx, ny) not in visited:
                        queue.append((nx, ny))
                        visited.add((nx, ny))

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands


