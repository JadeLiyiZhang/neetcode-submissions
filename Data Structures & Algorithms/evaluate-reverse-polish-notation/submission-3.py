class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return
        stack = []
        operations = ['+', '-', '*', '/']
        for token in tokens:
            if token in operations:
                num1 = stack.pop()
                num2 = stack.pop()
                if token == '+':
                    res = num1 + num2
                elif token == '-':
                    res = num2 - num1
                elif token == "*":
                    res = num1 * num2
                elif token == '/':
                    res = int(float(num2) / num1)
                stack.append(res)
            elif token not in operations:
                stack.append(int(token))
        return stack[-1]