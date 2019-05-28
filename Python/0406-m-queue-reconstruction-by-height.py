class Solution_1:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if not people:
            return []
        
        # obtain everyone's info
        # key=height, value=k-value, index in original array
        peopledict, height, res = {}, [], []

        for i in range(len(people)):
            p = people[i]
            if p[0] in peopledict:
                peopledict[p[0]].append((p[1], i))
            else:
                peopledict[p[0]] = [(p[1], i)]
                height.append(p[0])

        height.sort()

        for h in height[::-1]:
            peopledict[h].sort()
            for p in peopledict[h]:
                res.insert(p[0], people[p[1]])

        return res


class Solution_2:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        t = sorted(people, key=lambda x: (-x[0], x[1]))

        res = []
        for (h, k) in t:
            res.insert(k, (h, k))

        return res
