class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid = set()
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            if t[0] == target[0]:
                valid.add(0)
            if t[1] == target[1]:
                valid.add(1)
            if t[2] == target[2]:
                valid.add(2)
        
        return len(valid) == 3