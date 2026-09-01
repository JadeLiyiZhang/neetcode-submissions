from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.storage = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage:
            return ""
        
        possible_timestamps = [ts for ts in self.storage[key] if ts <= timestamp]
        if not possible_timestamps:
            return ""

        closest_timestamp = max(possible_timestamps)
        return self.storage[key][closest_timestamp]
