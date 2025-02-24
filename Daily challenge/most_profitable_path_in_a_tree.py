class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        #build the adjacency list

        adj=defaultdict(list)

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        # use dfs to find bob's path to the root
        # I need a hashmap to keep track of the time taken for bob to reach a certain node

        time_taken_by_bob={}
        # function will take in the node,prev node and the time
        def dfsBob(src,prev,time):
            if src==0:
                time_taken_by_bob[src]=time

                return True

            for neighbor in adj[src]:
                if neighbor==prev:
                    continue
                if dfsBob(neighbor,src, time + 1):
                    time_taken_by_bob[src]=time
                    return True

            return False

        dfsBob(bob,-1,0)

        # alice's traversal,bfs cause she can go in all directions

        q=deque([(0,-1,0,amount[0])]) #root,parent,time taken and total profit
        res=float("-inf")

        while q:
            node,parent,time,profit=q.popleft()
            

            for neighbor in adj[node]:
                if neighbor ==parent:
                    continue
                neighbor_time=time+1
                neighbor_profit=amount[neighbor]

                if neighbor in time_taken_by_bob:
                    if neighbor_time>time_taken_by_bob[neighbor]:
                        neighbor_profit=0

                    if neighbor_time==time_taken_by_bob[neighbor]:
                        neighbor_profit//=2

                q.append((neighbor,node,neighbor_time,profit+neighbor_profit))
                if len(adj[neighbor])==1:
                    res=max(res,profit+neighbor_profit)
        return res



         
