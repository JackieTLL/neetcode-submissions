class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        # check rows
        for row in range(rows):
            rowSet = set()
            for col in range(cols):
                if board[row][col] !='.':
                    if board[row][col] not in rowSet:
                        rowSet.add(board[row][col])
                    else:
                        return False
        # check cols
        for col in range(cols):
            colSet = set()
            for row in range(rows):
                if board[row][col] != '.':
                    if board[row][col] not in colSet:
                        colSet.add(board[row][col])
                    else:
                        return False
        # check small grid
        for startRow in range(0, 9, 3):
            for startCol in range(0, 9, 3):
                gridSet = set()
                for i in range(3):
                    for j in range(3):
                        if board[startRow + i][startCol + j] != '.':
                            if board[startRow + i][startCol + j] not in gridSet:
                                gridSet.add(board[startRow + i][startCol + j])
                            else:
                                return False
        return True

