class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            count = 0
            flag = False
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] <= temperatures[i]:
                    count += 1
                if temperatures[j] > temperatures[i]:
                    count += 1
                    flag = True
                    break
            if flag:
                res[i] = count
        return res
