class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        ROWS,COLS=len(isWater),len(isWater[0])

        q=deque()

        res=[[-1]*COLS for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                if isWater[r][c]:
                    q.append((r,c))
                    res[r][c]=0

        while q:
            r,c=q.popleft()
            height=res[r][c]
            neighbors=[[r+1,c],[r-1,c],[r,c-1],[r,c+1]]

            for neighbor_row,neighbor_col in neighbors:
                if (
                    neighbor_row<0 or neighbor_col<0 or
                    neighbor_row==ROWS or neighbor_col==COLS or
                    res[neighbor_row][neighbor_col]!=-1

                ):
                    continue

                q.append((neighbor_row,neighbor_col))
                res[neighbor_row][neighbor_col]=height+1


        return res