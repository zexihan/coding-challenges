# extremely slow but straightforward
class Solution_1(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or not costs[0]:
            return 0
        for i in range(1, len(costs)):
            for j in range(len(costs[0])):
                costs[i][j] += min(costs[i - 1][:j] + costs[i - 1][j + 1:])
        return min(costs[-1])


class Solution_2(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or not costs[0]:
            return 0
        
        rows = len(costs)
        columns = len(costs[0])

        costMatrix = [[0] * columns for r in range(rows)]
        costMatrix[0] = costs[0][:]

        for i in range(1, rows):
            for j in range(columns):
                tempRow = costMatrix[i - 1][:]
                tempRow.pop(j)
                costMatrix[i][j] = min(tempRow) + costs[i][j]

        res = min(costMatrix[rows - 1])
        return res
