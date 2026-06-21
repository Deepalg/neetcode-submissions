from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=len(board)
        columns=len(board[0])
        row_dict=defaultdict(list)
        column_dict=defaultdict(list)
        grid_dict=defaultdict(list)

        for i in range(rows):
            for j in range(columns):
                if board[i][j]==".":
                    continue


                if i in row_dict:
                    if board[i][j] in row_dict[i]:
                        return False
                    else:
                        row_dict[i].append(board[i][j])
                else:
                    row_dict[i].append(board[i][j])


                if j in column_dict:
                    if board[i][j] in column_dict[j]:
                        return False
                    else:
                        column_dict[j].append(board[i][j])
                else:
                    column_dict[j].append(board[i][j])
                
                if (i//3,j//3) in grid_dict:
                    if board[i][j] in grid_dict[(i//3,j//3)]:
                        return False
                    else:
                        grid_dict[(i//3,j//3)].append(board[i][j])
                else:
                    grid_dict[(i//3,j//3)].append(board[i][j])

        return True
                
        