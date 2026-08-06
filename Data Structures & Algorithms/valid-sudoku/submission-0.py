class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            cleanedrow = []
            for num in row:
                if num.isnumeric():
                    cleanedrow.append(num)        
            if len(set(cleanedrow)) < len(cleanedrow):
                return False
        column_dict = defaultdict(list)
        col_list = []
        for i in range(9):
            for j in range(9):
                if board[j][i].isnumeric():
                    col_list.append(board[j][i])
            column_dict[i] = col_list
            col_list = []
        for key in column_dict.keys():
            if len(set(column_dict[key])) < len(column_dict[key]):
                return False
        # Check 3x3 sub-boxes
        for r_start in (0, 3, 6):
            for c_start in (0, 3, 6):
                box_vals = []
                for i in range(3):
                    for j in range(3):
                        val = board[r_start + i][c_start + j]
                        if val.isnumeric():
                            box_vals.append(val)
                if len(set(box_vals)) < len(box_vals):
                    return False

        return True

        


