class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join([f"{len(w)}${w}" for w in strs])

    def decode(self, s: str) -> List[str]:
        print(s)
        output = []
        i = 0
        l = ''
        while i < len(s):
            c = s[i]
            if c == "$":
                n = int(l)
                output.append(s[i+1:n+i+1])

                l = ''
                i += n + 1
            else:
                l += s[i]
                i += 1
        return output
    

