class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def findStarts(board, word):
            res = []
            rows, cols = len(board), len(board[0])
            for row in range(rows):
                for col in range(cols):
                    if board[row][col] == word[0]:
                        res.append((row, col))
            return res

        def solve(row, col, board, word, chosen):
            rows, cols = len(board), len(board[0])
            if word == "":
                return True
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for direction in directions:
                newRow, newCol = row + direction[0], col + direction[1]
                if ((0 <= newRow < rows) and 
                    (0 <= newCol < cols and
                    board[newRow][newCol] == word[0]) and
                    chosen[newRow][newCol] == 0):
                    first = word[0]
                    chosen[newRow][newCol] = 1
                    solution = solve(newRow, newCol, board, word[1:], chosen)
                    if solution:
                        return solution
                    chosen[newRow][newCol] = 0
            return False
        starts = findStarts(board, word)
        rows, cols = len(board), len(board[0])
        chosen = [[0] * cols for _ in range(rows)]
        for row, col in starts:
            chosen[row][col] = 1
            isexist = solve(row, col, board, word[1:], chosen)
            if isexist:
                return True
            chosen[row][col] = 0
        return False

        

        