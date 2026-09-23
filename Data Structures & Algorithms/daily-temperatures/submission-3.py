from abc import abstractproperty
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while s and t > temperatures[s[-1]]:
                prev_i = s.pop()
                res[prev_i] = i - prev_i
            s.append(i)
        return res
