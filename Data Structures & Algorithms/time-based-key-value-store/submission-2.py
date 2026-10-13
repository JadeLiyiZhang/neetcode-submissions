class TimeMap:

    def __init__(self):
        self.map = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key][timestamp] = value

    
    def searchPrev(self, timestamps, target):
        left, right = 0, len(timestamps) - 1
        res = float('-inf')
        while left <= right:
            mid = left + (right - left) // 2
            if timestamps[mid] == target:
                return target
            elif timestamps[mid] < target:
                res = max(res, timestamps[mid])
                left = mid + 1
            else:
                right = mid - 1
        return res if res != float('-inf') else -1


    def get(self, key: str, timestamp: int) -> str:
        if timestamp in self.map[key]:
            return self.map[key][timestamp]
        
        else:
            time_dict = self.map[key]
            keys = sorted(time_dict.keys())
            target = self.searchPrev(keys, timestamp)
            if target == -1:
                return ''
            else:
                return self.map[key][target]
            