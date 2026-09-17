class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        if len(set(temperatures)) == 1:
            return res

        for i, t in enumerate(temperatures):
            n = 0
            for s in stack:
                if t > s[0]:
                    res[s[1]] = i - s[1]
                    n += 1
            for _ in range(n):
                print(n)
                stack.pop()
            stack.append((t, i))
        return res