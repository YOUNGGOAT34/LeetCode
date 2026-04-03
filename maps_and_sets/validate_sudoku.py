class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #validate rows
        for row in range(9):
            seen=set()
            for col in range(9):
                cell=board[col][row]
                if cell in seen:
                    return False
                if cell !=".":
                    seen.add(cell)

        #validate cols
        for row in range(9):
            seen=set()
            for col in range(9):
                    cell=board[col][row]

                    if cell in seen:
                        return False
                    if cell!=".":
                        seen.add(cell)

        #validate boxes

        starting_cells=[
            (0,0),(0,3),(0,6),
            (3,0),(3,3),(3,6),
            (6,0),(6,3),(6,6)
        ]

        for row,col in starting_cells:
            seen=set()

            for r in range(row,row+3):
                for c in range(col,col+3):
                    cell=board[r][c]

                    if cell in seen:
                        return False

                    if cell!=".":
                        seen.add(cell)

        return True
             

