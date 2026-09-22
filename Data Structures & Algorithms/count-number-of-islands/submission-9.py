from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == [[]]:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islandNum = 0
        def bfs(row, col):
            q = deque()
            visited.add((row, col))
            q.append((row, col))
            while q:
                r, c = q.popleft()
                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for dr, dc in directions:
                    newR, newC = r + dr, c + dc
                    if (newR in range(rows) and
                    newC in range(cols) and
                    grid[newR][newC] == "1" and
                    (newR, newC) not in visited):
                        q.append((newR, newC))
                        visited.add((newR, newC))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    islandNum += 1
                    bfs(row, col)
        return islandNum