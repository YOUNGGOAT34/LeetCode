from collections import defaultdict
from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=defaultdict(list)
        for to,fr in edges:
            adj[to].append(fr)
            adj[fr].append(to)

        def dfs(node):
            nodes=1
            edges=len(adj[node])
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor in visited:
                    continue
                
                sub_edges,sub_nodes=dfs(neighbor)
                edges+=sub_edges
                nodes+=sub_nodes
            return edges,nodes

        res=0

        visited=set()

        for node in range(n):
            if node in visited:
                continue
            
           

            edges,nodes=dfs(node)
            edges//=2
            if edges==(nodes*(nodes-1))//2:
                res+=1

        return res



        