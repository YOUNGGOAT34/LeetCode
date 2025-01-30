
class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj=defaultdict(list)

        for node1,node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        def get_longest_path(node):
            

            q=deque()

            q.append((node,1))
            dist={node:1}
            while q:
                n,d=q.popleft()

                for nei in adj[n]:
                    if nei in dist:
                        if dist[nei]==d:
                           return -1
                        continue
                        

                    q.append((nei,d+1))
                    dist[nei]=d+1

            return max(dist.values())

        
        def get_connected_component(node):
            component=set([node])

            q=deque()
            q.append(node)
            

            while q:
                n=q.popleft()

                for nei in adj[n]:
                    if nei not in component:
                        q.append(nei)
                        component.add(nei)
                        visited.add(nei)

            return component




        

        res=0

       
        visited=set()
        for i in range(1,n+1):
            if i in visited:
                continue
            visited.add(i)
            connected_component=get_connected_component(i)
            max_count=0
            for src in connected_component:
                longest_path=get_longest_path(src)
                if longest_path==-1:
                    return -1
                max_count=max(max_count,longest_path)

            res+=max_count

        return res
