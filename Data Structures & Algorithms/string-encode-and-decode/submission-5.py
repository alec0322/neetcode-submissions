class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""

        for s in strs:
            encodedString += f"#{len(s)}#{s}"
        
        return encodedString

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        strs = []
        i = 1
        while i < len(s):
            cur, n = "", ""

            while i < len(s) and s[i].isnumeric():
                n += s[i]
                i += 1
            
            n = int(n)
            i += 1

            for j in range(n):
                cur += s[i + j]
            strs.append(cur)
            
            i += n + 1
        
        return strs
