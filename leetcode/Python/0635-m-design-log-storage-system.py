class LogSystem:

    def __init__(self):
        self.logs = {}
        self.graMap = {'Year': 1, 'Month': 2, 'Day': 3,
                  'Hour': 4, 'Minute': 5, 'Second': 6}

    def put(self, id: int, timestamp: str) -> None:
        t = tuple(timestamp.split(':'))
        self.logs[t] = id

    def retrieve(self, s: str, e: str, gra: str) -> List[int]:
        idx = self.graMap[gra]
        s = tuple(s.split(':')[:idx])
        e = tuple(e.split(':')[:idx])

        res = []
        for t, id in self.logs.items():
            if s <= t[:idx] <= e:
                res.append(id)
        return res


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)
