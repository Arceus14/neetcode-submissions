class TimeMap:

    def __init__(self):
        self.hmap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # Use binary search to look for key
        res = ''
        lst = self.hmap[key]
        low, high = 0, len(lst)

        while low < high:
            mid = (low + high) // 2
            ts, value = lst[mid]
            if ts <= timestamp:
                res = value
                low = mid + 1
            elif ts > timestamp:
                high = mid
            
        return res
