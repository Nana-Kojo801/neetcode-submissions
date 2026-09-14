class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for w in strs:
            s = ''.join(sorted(w))

            d[s] = d.get(s, []) + [w]

        return [d[k] for k in d]
