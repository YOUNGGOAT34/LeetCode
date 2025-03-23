from collections import defaultdict
import heapq
from typing import List


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj=defaultdict(list)
        for src,dst,weight in roads:
            adj[src].append([dst,weight])
            adj[dst].append([src,weight])
        heap=[]
        
        mod = 10**9 + 7

        

        min_cost={i: float('inf') for i in range(n)}
        min_cost[0]=0
        number_of_ways=[0]*n
        number_of_ways[0]=1
       
       
        heapq.heappush(heap,(0,0))
        
        while heap:
            cost,current_node=heapq.heappop(heap)

            if cost > min_cost[current_node]:
                continue

            for nei,weight in adj[current_node]:
                new_cost=weight+cost
               
                
                if new_cost<min_cost[nei]:
                    min_cost[nei]=new_cost
                    number_of_ways[nei]=number_of_ways[current_node] #reset the number of ways
                    heapq.heappush(heap,(new_cost,nei)) #push the new neighbor and the cost to the heap

                elif new_cost == min_cost[nei]:  
                    number_of_ways[nei] = (number_of_ways[nei] + number_of_ways[current_node]) % mod


        return number_of_ways[-1]



        