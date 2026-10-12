class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g = defaultdict(list)

        for w in strs:
            p = [0] * 26
            for c in w:
                p[ord('a') - ord(c)] += 1
            g[tuple(p)].append(w)
        return (list(g.values()))