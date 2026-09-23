class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for token in tokens:
            if token not in "+-*/":
                s.append(int(token))
                continue
            num1 = s.pop()
            num2 = s.pop()
            if token == "+":
                s.append(num1 + num2)
            elif token == '-':
                s.append(num2 - num1)
            elif token == "*":
                s.append(num1 * num2)
            else:
                s.append(int(num2/num1))
        return sum(s)