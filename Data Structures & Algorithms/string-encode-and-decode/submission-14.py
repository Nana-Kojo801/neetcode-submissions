class Solution:

    def encode(self, strs: List[str]) -> str:
        # "4#Hello5#World"
        return ''.join([ f"{len(w)}#{w}" for w in strs ])

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        l = ''

        while i < len(s):
            c = s[i]
            if c != "#":
                l += s[i]
                i += 1
            else:
                n = int(l)
                res.append(s[i+1:i+1+n])

                l = ''
                i += n + 1
        return res
            