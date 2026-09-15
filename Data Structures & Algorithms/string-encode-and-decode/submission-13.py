class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join([f"{len(s)}#{s}" for s in strs])

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        print(s)
        while i < len(s) - 1:
            l = ''
            while i < len(s) and s[i] != "#":
                print(s[i])
                l += s[i]
                i += 1
            print(l)
            output.append(s[i+1 : i + int(l)+1])
            i += int(l) + 1
            l = ''
        return output
            
