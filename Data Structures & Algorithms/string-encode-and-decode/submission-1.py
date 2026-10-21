class Solution:

    def encode(self, strs: List[str]) -> str:
        t = ""

        for s in strs:
            t += f"{len(s)}#{s}#"
        
        return t

    def decode(self, s: str) -> List[str]:
        strs = []
        s_list = list(s)
        while s_list:
            count = ""
            while s_list[0].isnumeric():
                count += s_list.pop(0)
            s_list.pop(0)
            t = ""
            for j in range(int(count)):
                t += s_list.pop(0)
            strs.append(t)
            s_list.pop(0)
        
        return strs