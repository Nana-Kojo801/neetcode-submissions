class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        max_area = 0

        # [2, 1, 5, 6, 2, 3]
        # [(0, 1), (2, 5), ]
        # area = (4 - 3) * 6
        for i, h in enumerate(heights):
            idx = i
            while s and h < s[-1][1]:
                si, sh = s[-1]
                area = (i - si) * sh
                max_area = max(area, max_area)
                s.pop()
                idx = si
            s.append((idx, h))
        
        while s:
            si, sh = s[-1]
            area = (len(heights) - si) * sh
            max_area = max(area, max_area)
            s.pop()
        
        return max_area