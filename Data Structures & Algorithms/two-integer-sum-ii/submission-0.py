class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        table = {}
        for i in range(len(numbers)):
            if target - numbers[i] not in table:
                table[numbers[i]] = i + 1
            else:
                return [table[target - numbers[i]], i + 1]