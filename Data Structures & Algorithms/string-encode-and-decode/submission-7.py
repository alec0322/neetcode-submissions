class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += f'#{len(s)}#{s}'
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []

        i = 1
        while i < len(s):
            count = 0
            while i < len(s) and s[i].isnumeric():
                digit = int(s[i])
                count = (count * 10) + digit
                i += 1
            
            i += 1
            t = ""
            length = i + count
            while i < length:
                t += s[i]
                i += 1
            decoded.append(t)
                
            i += 1
        
        return decoded