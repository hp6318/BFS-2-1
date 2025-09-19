"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

'''
Solution 1: BFS
iterate over each neighbors, neighbor's neighbors.... starting from given employee id
whose importance needs to be found. This means, we need to build the graph/tree.
For finding edges(neighbors/subordinates), we need to have an adjacency list/map.
For saving space, since the *Employee node objects are already created and provided
as input, we create a map of {id - *Employee object}. 
Time Complexity: O(N) - N employees, we might have to traverse each employee all subordinates
                        report to target employee whose imporatnce needs to be found
Space Complexity: O(N) - bfs queue
'''
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        employees_map = {} # id - Object *Employee
        for employee in employees:
            employees_map[employee.id] = employee
        
        bfs_queue = deque()
        visited = set()
        
        bfs_queue.append(id) # add the employee's id whose importance needs to be found
        visited.add(id)

        importance = 0

        while (len(bfs_queue)!=0):
            parent_id =  bfs_queue.popleft()
            importance += employees_map[parent_id].importance # add the importance

            if employees_map[parent_id].subordinates is not None:  
                for neigh_id in employees_map[parent_id].subordinates:
                    if neigh_id not in visited:
                        bfs_queue.append(neigh_id)
                        visited.add(neigh_id) # mark visited
        
        return importance 

'''
Solution 2: DFS
iterate over each neighbors, neighbor's neighbors.... starting from given employee id
whose importance needs to be found. This means, we need to build the graph/tree.
For finding edges(neighbors/subordinates), we need to have an adjacency list/map.
For saving space, since the *Employee node objects are already created and provided
as input, we create a map of {id - *Employee object}. 
Time Complexity: O(N) - N employees, we might have to traverse each employee all subordinates
                        report to target employee whose imporatnce needs to be found
Space Complexity: O(N) - DFS stack
'''
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        employees_map = {} # id - Object *Employee
        for employee in employees:
            employees_map[employee.id] = employee
        
        self.importance = 0
        self.helper(employees_map, id) 

        return self.importance

    def helper(self,employees_map,id):
        # base
        # handles under for loop

        # logic
        self.importance+=employees_map[id].importance
        if employees_map[id].subordinates is not None:
            for subordinate_id in employees_map[id].subordinates:
                self.helper(employees_map,subordinate_id)
