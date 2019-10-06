"""
Greedy
freq(A) = k >= freq(B) >= ... >= freq(z), p tasks has the same freq as A
A B C ... A B idle ... ... A ...
  n slots   n slots          p tasks
    k - 1 groups
res = (k - 1) * (n + 1) + p

Special case: # tasks > res
We can schedule most frequent tasks without idling
=> we can schedule all the tasks without idling
=> res = # of tasks
"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord("A")] += 1
        max_count = max(count)
        res = (max_count - 1) * (n + 1)
        p = 0
        for c in count:
            p = p + 1 if max_count == c else p
        return max(len(tasks), res + p)

