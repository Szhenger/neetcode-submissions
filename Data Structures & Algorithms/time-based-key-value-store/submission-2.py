class TimeMap:

    def __init__(self):
        self.timMap = defaultdict(list) 

    def set(self, key: str, val: str, timestamp: int) -> None:
        self.timMap[key].append((timestamp, val))

    def get(self, key: str, timestamp: int) -> str:
        val, vals = "", self.timMap[key]
        left, right = 0, len(vals) - 1
        while left <= right:
            middle = (left + right) // 2
            if vals[middle][0] <= timestamp:
                val = vals[middle][1]                
                left = middle + 1            
            else:
              right = middle - 1
        return val

