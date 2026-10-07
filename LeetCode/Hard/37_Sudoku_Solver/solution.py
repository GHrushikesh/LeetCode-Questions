class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        # Track numbers already used in each row
        rowUsed = [[False] * 10 for _ in range(9)]
        # Track numbers already used in each column
        colUsed = [[False] * 10 for _ in range(9)]
        # Track numbers already used in each 3x3 box
        boxUsed = [[False] * 10 for _ in range(9)]
        # Fill the tracking arrays with existing numbers
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    box = (i // 3) * 3 + (j // 3)
                    rowUsed[i][num] = True
                    colUsed[j][num] = True
                    boxUsed[box][num] = True
        def solve():
            # Find an empty cell
            row = -1
            col = -1
            found = False
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        row = i
                        col = j
                        found = True
                        break
                if found:
                    break
            # No empty cell >> solved
            if not found:
                return True
            box = (row // 3) * 3 + (col // 3)
            # Try numbers 1 to 9
            for num in range(1, 10):
                # Check row, column and box in O(1)
                if rowUsed[row][num]:
                    continue
                if colUsed[col][num]:
                    continue
                if boxUsed[box][num]:
                    continue
                # Place number
                board[row][col] = str(num)
                rowUsed[row][num] = True
                colUsed[col][num] = True
                boxUsed[box][num] = True
                # Solve next empty cell
                if solve():
                    return True
                # Backtrack
                board[row][col] = '.'
                rowUsed[row][num] = False
                colUsed[col][num] = False
                boxUsed[box][num] = False
            return False

        solve()