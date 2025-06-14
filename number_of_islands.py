#Number of Islands - 1337c0de #200

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> str:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        result = 0


        def dfs(r,c):
            if (r, c) in visited:
                return
            
            visited.add((r,c))

            directions = [[1,0], [-1, 0], [0,1], [0,-1]]

            for rd, cd in directions:
                nr = r + rd
                nc = c + cd

                if (nr in range(rows) and
                    nc in range(cols) and
                    grid[nr][nc] == "1"):
                        #if new grid point is a 1 signyfing it is an island 
                        #continue in that directions
                    dfs(nr,nc)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    result += 1
        
        return result
    
    # #####BFS####### class Solution:
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     ROWS,COLS = len(grid), len(grid[0])
    #     visited = set()
    #     num_islands = 0

    #     def bfs(r,c):
    #         q = collections.deque()
    #         visited.add((r, c))
    #         q.append((r, c))

    #         while q:
    #             row, col = q.popleft()
    #             directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
                
    #             for dr, dc in directions:
    #                 r, c = row + dr, col + dc
    #                 if (r in range(ROWS) and
    #                     c in range(COLS) and
    #                     grid[r][c] == "1" and  #is a land position
    #                     (r, c) not in visited):
    #                     q.append((r, c))
    #                     visited.add((r, c))

    #     for r in range(ROWS):
    #         for c in range(COLS):
    #             if grid[r][c] == "1" and (r, c) not in visited:
    #                 bfs(r, c)
    #                 num_islands += 1
    #     return num_islands
        