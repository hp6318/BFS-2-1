'''
Solution 1: BFS
- Maintain size variable in order to do a level order traversal. 
Time complexity: O(m*n) - we visit each cell one time
Space Complexity: O(m*n) - size of queue, Worst case, when all oranges are rotten at first, 
                            we fill up the queue with all cells
                    
'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_oranges = 0
        m=len(grid)
        n=len(grid[0])

        bfs = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    #rotten
                    bfs.append((i,j))
                elif grid[i][j]==1:
                    #fresh
                    fresh_oranges+=1
        
        if fresh_oranges==0: # if there no fresh oranges to be rotten. 
            return 0
        if len(bfs)==0: # I don't have a single rotten orange to spoil others.
            return -1

        neigh = [[0,-1],[-1,0],[0,1],[1,0]]
        minutes=0
        while bfs:
            size = len(bfs)
            for i in range(size):
                pivot_r,pivot_c = bfs.popleft()
                for neighbor in neigh:
                    n_r,n_c = pivot_r+neighbor[0], pivot_c+neighbor[1]
                    #sanity check
                    if n_r>=0 and n_r<=m-1 and n_c>=0 and n_c<=n-1:
                        if grid[n_r][n_c]==1:
                            bfs.append([n_r,n_c])
                            fresh_oranges-=1
                            grid[n_r][n_c]=2 # mark visited
                            
            minutes+=1
        
        if fresh_oranges>0: # not all rotten
            return -1
        
        return minutes-1 # in the while loop, minutes counter will move 1 step ahead

'''        
Solution 1: DFS + DP (inherently captured)
grid behaves as dp matrix itself. as we iterate to next rotten orange(original), traversal
through the grid reduces as matrix already keeps optimizing to best state. 
Time complexity: 
    - Tempting to say, 4^(m*n) - explore all paths from each grid cell. 
    - Actual = O(m*n) - behaves as DP (repeated sub-problems) and traversal limits to k*m*n,
                        where k = small constant and can be ignored. 
Space Complexity: O(m*n) - size of recursive stack.                     
'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [[0,-1],[-1,0],[0,1],[1,0]] # left, top, right, bottom
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2: # make recursive call when we have a rotten orange
                    self.helper(i,j,grid,2,directions) # row, col, grid, time, directions
        
        minutes = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    # still fresh
                    return -1
                minutes = max(minutes,grid[i][j])
        if minutes==0:
            return 0
        return minutes -2 # offset
    
    def helper(self,row,col,grid,time, directions):
        # base
        # not needed, handled inside for loop. 
        # logic
        grid[row][col] = time
        for direction in directions:
            n_r, n_c = row+direction[0], col+direction[1]
            if 0<=n_r<len(grid) and 0<=n_c<len(grid[0]):
                if grid[n_r][n_c]==1: # still fresh, go rot it
                    self.helper(n_r,n_c,grid,time+1, directions)
                elif grid[n_r][n_c]>time+1: # if it takes lesser time, only then traverse
                    self.helper(n_r,n_c,grid,time+1, directions)
        