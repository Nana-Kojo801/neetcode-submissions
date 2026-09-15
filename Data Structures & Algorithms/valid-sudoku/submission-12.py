class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, 6, 3):
            for j in range(0, 6, 3):
                chars = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]
                new_chars = [c for c in chars if c != "."]

                if len(set(new_chars)) != len(new_chars):
                    return False
        
        for i in range(9):
            chars = [board[j][i] for j in range(9)]
            new_chars = [c for c in chars if c != "."]

            if len(set(new_chars)) != len(new_chars):
                return False

        for i in range(9):
            chars = board[i]
            new_chars = [c for c in chars if c != "."]

            if len(set(new_chars)) != len(new_chars):
                return False
        return True

