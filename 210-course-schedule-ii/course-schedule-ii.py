class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses
        for a, b in prerequisites:        # b before a
            adj[b].append(a)              # b unlocks a
            indegree[a] += 1

        q = [i for i in range(numCourses) if indegree[i] == 0]
        i = 0                             # next position to process
        while i < len(q):
            cur = q[i]
            i += 1
            for nxt in adj[cur]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        return q if len(q) == numCourses else []