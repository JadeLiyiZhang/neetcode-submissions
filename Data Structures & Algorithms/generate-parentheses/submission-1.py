class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtracking(left, right, s):
            if left == n and right == n:
                res.append(''.join(s))
                return
            
            if left < n:
                s.append('(')
                backtracking(left + 1, right, s)
                s.pop()
            
            if right < left:
                s.append(')')
                backtracking(left, right+ 1, s)
                s.pop()
        
        backtracking(0, 0, [])
        return res