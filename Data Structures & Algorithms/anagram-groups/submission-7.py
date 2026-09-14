class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for w in strs:
            count = [0] * 26

            for c in w:
                count[ord(c) - ord('a')] += 1
            
            d[tuple(count)].append(w)
        
        return [d[k] for k in dict(d)]
