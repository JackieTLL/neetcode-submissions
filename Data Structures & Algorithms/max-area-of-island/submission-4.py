from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = deque()
        def bfs(row, col):
            area = 0
            q.append((row, col))
            visited.add((row, col))
            while q:
                row, col = q.popleft()
                area += 1
                for dr, dc in directions:
                    newRow, newCol = row + dr, col + dc
                    if (newRow in range(rows) and
                    newCol in range(cols) and 
                    grid[newRow][newCol] == 1 and
                    (newRow, newCol) not in visited):
                        q.append((newRow, newCol))
                        visited.add((newRow, newCol))
            return area
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    res = max(res, bfs(row, col))
        return res
                
        
        