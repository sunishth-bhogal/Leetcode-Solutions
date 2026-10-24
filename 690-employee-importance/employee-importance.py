"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        lookup = {}
        for emp in employees:
            lookup[emp.id] = emp
        
        def dfs(eid):
            emp = lookup[eid]
            total = emp.importance 
            for sub in emp.subordinates:
                total += dfs(sub)
            return total
        
        return dfs(id)

        