# Time: O(n^2) 275ms
# Space: O(1) 
"""
DFS
Find an entrance of an island
Remove the island using DFS
Counting the number of removed islands
"""
class Solution_1(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0

        count = 0
        row, col = len(grid), len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    self.removeIsland(grid, row, col, i, j)
                    count += 1
        return count

    def removeIsland(self, grid, row, col, x, y):
        grid[x][y] = '0'

        for i in range(-1,2):
            for j in range(-1, 2):
                if self.isValid(i, j, x, y, row, col) and grid[x + i][y + j] == '1':
                    self.removeIsland(grid, row, col, x + i, y + j)
    
    def isValid(self, i, j, x, y, row, col):
        return abs(i) != abs(j) and x + i >=0 and x + i < row and y + j >=0 and y + j < col

# Time: 82ms
# BFS
class Solution_2(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        
        m, n = len(grid), len(grid[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                else:
                    count += 1
                    stack = [[i, j]]
                    
                    while len(stack) != 0:
                        p, q = stack.pop()
                        
                        if p >= 1 and grid[p-1][q] == '1':
                            stack.append([p-1,q])
                        if p < m-1 and grid[p+1][q] == '1':
                            stack.append([p+1,q])
                        if q >= 1 and grid[p][q-1] == '1':
                            stack.append([p, q-1])
                        if q < n-1 and grid[p][q+1] == '1':
                            stack.append([p, q+1])
                        
                        grid[p][q] = '0'
        return count


if __name__ == "__main__":
    new_1 = Solution_1()
    new_2 = Solution_2()
    print(new_1.numIslands([['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']])) # 3
    print(new_2.numIslands([['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']])) # 3