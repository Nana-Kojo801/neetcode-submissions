class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, len(board) - 3, 3):
            for j in range(0, len(board[i]) - 3, 3):
                chars = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]
                new_chars = [c for c in chars if c != "."]

                if len(set(new_chars)) != len(new_chars):
                    print("3x3")
                    return False
        
        for i in range(len(board)):
            chars = [board[j][i] for j in range(len(board))]
            new_chars = [c for c in chars if c != "."]

            if len(set(new_chars)) != len(new_chars):
                print("Column")
                return False

        for i in range(len(board)):
            chars = board[i]
            new_chars = [c for c in chars if c != "."]

            if len(set(new_chars)) != len(new_chars):
                print("Row")
                return False
        return True

