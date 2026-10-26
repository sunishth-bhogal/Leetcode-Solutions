class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        unlocks = {i: [] for i in range(numCourses)}
        need = [0] * numCourses

        for crs, pre in prerequisites:
            unlocks[pre].append(crs)
            need[crs] += 1

        ready = [c for c in range(numCourses) if need[c] == 0]
        i = 0                          # next position to process in ready

        while i < len(ready):
            c = ready[i]
            i += 1
            for nxt in unlocks[c]:
                need[nxt] -= 1
                if need[nxt] == 0:
                    ready.append(nxt)  # list grows; the loop will reach it

        return len(ready) == numCourses