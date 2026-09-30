class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }
        res = []

        def backtracking(i, path):
            if i == len(digits):
                res.append(''.join(path))
                return
            
            
            for char in mapping[int(digits[i])]:
                path.append(char)
                backtracking(i + 1, path)
                path.pop()
        
        backtracking(0, [])
        return res