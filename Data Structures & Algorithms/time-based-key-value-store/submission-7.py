class TimeMap:

    def __init__(self):
        self.timMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        val, vals = "", self.timMap[key]
        l, r = 0, len(vals) - 1
        while l <= r:
            m = (l + r) // 2
            if vals[m][0] <= timestamp:
                val = vals[m][1]
                l = m + 1
            else:
                r = m - 1
        return val
