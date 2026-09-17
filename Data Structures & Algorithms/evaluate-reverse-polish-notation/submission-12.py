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
                # print(f"{results[-2]} {token} {results[-1]} = {ans}")
                results.pop()
                results.pop()
                results.append(ans)
                # print(ans, token)
                """
                [10, 6, -132] /
                ans = 12 +
                ans = -132 *
                """
        return results[0]