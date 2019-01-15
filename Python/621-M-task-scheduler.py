class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord("A")] += 1
        max_count = max(count)
        res = (max_count - 1) * (n + 1)
        p = 0
        for c in count:
            p = p + 1 if max_count == c else p
        return max(len(tasks), res + p)

