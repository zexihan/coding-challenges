class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        pathCount = [0] * len(obstacleGrid[0])
        pathCount[0] = 1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1: pathCount[j] = 0
                elif j > 0: pathCount[j] += pathCount[j - 1]
        return pathCount[len(obstacleGrid[0]) - 1]