class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        n = len(equations)

        for i in range(n):
            a,b = equations[i]
            a_over_b = values[i]
            graph[a].append((b, a_over_b))

            b_over_a = 1/a_over_b
            graph[b].append((a, b_over_a))
        
        answers = []
        def dfs(multiplied_path, variable):
            if variable == y: return True, multiplied_path
            for neighbor, multiplier in graph[variable]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    found, path = dfs(multiplied_path * multiplier, neighbor)
                    if found: return True, path

            return False, -1
        
        for x,y in queries:
            if x not in graph or y not in graph:
                answers.append(-1)
            else:
                seen = set([x])
                found_answer, ans = dfs(1, x)
                answers.append(ans)
            
        return answers


        