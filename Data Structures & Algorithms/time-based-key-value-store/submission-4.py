class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.hashmap:
            return ""
        values = self.hashmap[key]

        l = 0
        r = len(values) - 1
        res = ""
        while l <= r:
            m = l + (r - l) // 2
            if values[m][0] == timestamp:
                return values[m][1]
            if values[m][0] > timestamp:
                r = m - 1
            elif values[m][0] < timestamp:
                l = m + 1
                res = values[m][1]
        return res