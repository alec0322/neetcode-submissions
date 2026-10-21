class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keyToAnagrams = defaultdict(list)

        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            keyToAnagrams[tuple(key)].append(s)
        
        return list(keyToAnagrams.values())