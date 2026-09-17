class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # if 0 <= len(tokens) <= 2:
        #     return int(tokens[0])
        stack = []
        operators = ['+', '-', '*', '/']

        for token in tokens:
            if token in operators:
                a = stack.pop()
                b = stack.pop()
                if token == "+":
                    stack.append(b + a)
                elif token == "-":
                    stack.append(b - a)
                elif token == "*":
                    stack.append(b * a)
                else:
                    stack.append(int(b / a))
            else:
                stack.append(int(token))
        return stack[0]