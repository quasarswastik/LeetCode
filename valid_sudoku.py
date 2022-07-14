class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_hash = collections.defaultdict(set)
        column_hash = collections.defaultdict(set)
        square_hash = collections.defaultdict(set)
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in row_hash[i] or 
                    board[i][j] in column_hash[j] or
                    board[i][j] in square_hash[(i//3, j//3)]):
                    return False
                row_hash[i].add(board[i][j])
                column_hash[j].add(board[i][j])
                square_hash[(i//3, j//3)].add(board[i][j])
        return True
