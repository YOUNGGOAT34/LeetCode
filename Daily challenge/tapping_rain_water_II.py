class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        ROWS,COLS=len(heightMap),len(heightMap[0])
        min_heap=[]
        # add border into min heap and mark as visited
        for row in range(ROWS):
            for col in range(COLS):
                if row in [0,ROWS-1] or col in [0,COLS-1]:
                    heappush(min_heap,(heightMap[row][col],row,col))
                    heightMap[row][col]=-1 # meaning it is visited
        # we need to go through the heap and visit the neighbors
        res=0
        max_h=0

        while min_heap:
            height,row,col=heappop(min_heap)

            max_h=max(max_h,height)

            res+=max_h-height


            neighbors=[[row+1,col],[row-1,col],[row,col+1],[row,col-1]]

            for neighbor_row,neighbor_col in neighbors:
                if (neighbor_row<0 or
                    neighbor_col<0 or
                    neighbor_row==ROWS or
                    neighbor_col==COLS or
                    heightMap[neighbor_row][neighbor_col]==-1 # visited
                ):
                   continue


                heappush(min_heap,(heightMap[neighbor_row][neighbor_col],neighbor_row,neighbor_col))
                heightMap[neighbor_row][neighbor_col]=-1



        return res








