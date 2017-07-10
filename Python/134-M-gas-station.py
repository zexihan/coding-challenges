# Time: O(n^2)
# Space: O(1)
# Time limit exceeded
class Solution_1(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):  
            return -1
        gas_left = 0
        for i in range(len(gas)):
            for j in range(len(gas)):
                if i + j < len(gas):
                    index = i + j
                else:
                    index = i + j - len(gas)
                gas_left += gas[index]
                cost_next = cost[index]
                if gas_left < cost_next:
                    break
                else:
                    gas_left -= cost_next
            gas_left = 0
            if j == len(gas) - 1:
                return i
        return -1

# Time: O(n)
# Space: O(1)
# Deque
class Solution_2(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):  
            return -1

        start = len(gas) - 1
        end = 0
        gas_left = gas[start] - cost[start]

        while end < start:
            # case 1: gas_left < 0 -> a new start needed
            if gas_left < 0:
                start -= 1
                gas_left += gas[start] - cost[start]
            # case 2: gas_left >= 0 -> try to move forward
            else:
                gas_left += gas[end] - cost[end]
                end += 1
        return start if sum >= 0 else -1




if __name__ == '__main__':
    new_1 = Solution_1()
    new_2 = Solution_1()
    print(new_1.canCompleteCircuit([3,4,3,6,7,1,2], [2,4,5,1,5,1,3]))
    print(new_2.canCompleteCircuit([3,4,3,6,7,1,2], [2,4,5,1,5,1,3]))