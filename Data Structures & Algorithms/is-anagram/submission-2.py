class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sFreq, tFreq = {}, {}

        for i, c in enumerate(s):
            sFreq[c] = sFreq.get(c, 0) + 1
            tFreq[t[i]] = tFreq.get(t[i], 0) + 1
        
        for c in sFreq:
            if sFreq[c] != tFreq.get(c, 0):
                return False
        
        return True
