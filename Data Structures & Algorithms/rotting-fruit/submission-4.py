class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        q = collections.deque()
        fresh = 0
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while fresh > 0 and q:
            qLen = len(q)
            for i in range(qLen):
                row, col = q.popleft()
                for dr, dc in directions:
                    newRow, newCol = row + dr, col + dc
                    if (newRow in range(rows) and
                    newCol in range(cols) and
                    grid[newRow][newCol] == 1):
                        grid[newRow][newCol] = 2
                        fresh -= 1
                        q.append((newRow, newCol))
            time += 1
        return time if fresh == 0 else -1