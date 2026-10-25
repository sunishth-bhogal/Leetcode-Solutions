class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))

        def dfs(node, parent, dist):
            if dist % signalSpeed == 0:
                count = 1
            else:
                count = 0
            for nxt, w in graph[node]:
                if nxt != parent:
                    count += dfs(nxt, node, dist + w)
            return count
        
        n = len(edges) + 1
        answer = [0] * n

        for c in range(n):
            pairs = seen = 0
            for nb, w in graph[c]:
                cnt = dfs(nb, c, w)
                pairs += seen * cnt
                seen += cnt
            answer[c] = pairs
        
        return answer
