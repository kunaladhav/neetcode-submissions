class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        l = len(board)

        # row
        for i in range(l):
            seen = set()

            for j in range(l):

                if board[i][j] == '.':
                    continue
                
                if board[i][j] in seen:
                    return False
                
                seen.add(board[i][j])

        # Column
        for i in range(l):
            seen = set()

            for j in range(l):

                if board[j][i] == '.':
                    continue
                
                if board[j][i] in seen:
                    return False
                
                seen.add(board[j][i])


        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):

                seen = set()

                for i in range(box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):

                        if board[i][j] == '.':
                            continue
                        if board[i][j] in seen:
                            return False
                        
                        seen.add(board[i][j])
        
        return True



