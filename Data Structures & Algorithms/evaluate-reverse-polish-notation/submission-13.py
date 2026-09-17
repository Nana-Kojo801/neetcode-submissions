class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1 or len(tokens) == 2:
            return int(tokens[0])
        
        results = []
        operators = ['+', '-', '*', '/']

        for i, token in enumerate(tokens):
            if token not in operators:
                results.append(int(token))
                continue
            if token in operators:
                ans = None
                if token == "+":
                    ans = results[-2] + results[-1]
                elif token == "-":
                    ans = results[-2] - results[-1]
                elif token == "*":
                    ans = results[-2] * results[-1]
                else:
                    ans = int(results[-2] / results[-1])
                results.pop()
                results.pop()
                results.append(ans)
        return results[0]