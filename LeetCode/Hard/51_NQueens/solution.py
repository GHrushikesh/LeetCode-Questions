class Solution: 
    def solveNQueens(self, n: int) -> list[list[str]]: 
        #Create empty chess board 
        board = [] 
        for i in range(n): 
            row = [] 
            for j in range(n): 
                row.append('.') 
            board.append(row) 
        result = [] 
        def isSafe(row, col): 
            i = row - 1 
            while i >= 0: 
                if board[i][col] == 'Q': 
                    return False  
                i -= 1 
            i = row - 1 
            j = col - 1 
            while i >= 0 and j >= 0: 
                if board[i][j] == 'Q': 
                    return False 
                i -= 1 
                j -= 1 
            i = row - 1 
            j = col + 1 
            while i >= 0 and j < n: 
                if board[i][j] == 'Q': 
                    return False 
                i -= 1 
                j += 1 
            return True 
        def solve(row): 
            # All queens have been successfully placed 
            if row == n: 
                solution = []
                for i in range(n): 
                    current_row = "" 
                    for j in range(n): 
                        current_row += board[i][j] 
                    solution.append(current_row) 
                result.append(solution) 
                return 
            for col in range(n): 
                if isSafe(row, col): 
                    board[row][col] = 'Q' 
                    solve(row + 1) 
                    # Backtrack: 
                    # Remove the queen 
                    board[row][col] = '.' 
        # Start from the first row
        solve(0) 
        return result