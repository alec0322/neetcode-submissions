class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # First, map each number to it's frequency
        freqMap = {}
        for n in nums:
            freqMap[n] = freqMap.get(n, 0) + 1
        
        # Then, export the map's items as tuples
        tuples = list(freqMap.items()) # [(n, freq), ...]

        # Lastly, sort the tuples by the freq
        tuples.sort(key=lambda x:x[1], reverse=True)
        
        return [tuples[i][0] for i in range(k)]