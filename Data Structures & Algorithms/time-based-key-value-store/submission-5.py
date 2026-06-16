class TimeMap:

    def __init__(self):
        # Initialize a default dictionary of empty lists
        self.timMap = defaultdict(list) 

    def set(self, key: str, val: str, timestamp: int) -> None:
        # Set the key list to append (timestamp, val) tuple
        self.timMap[key].append((timestamp, val))

    def get(self, key: str, timestamp: int) -> str:
        # Get the key list of (timestamp, val) tuples 
        val, vals = "", self.timMap[key]
        # Binary search greatest val less than or equal to timestamp 
        left, right = 0, len(vals) - 1
        while left <= right:
            middle = (left + right) // 2
            if vals[middle][0] <= timestamp:
                val = vals[middle][1]                
                left = middle + 1            
            else:
              right = middle - 1
        return val

