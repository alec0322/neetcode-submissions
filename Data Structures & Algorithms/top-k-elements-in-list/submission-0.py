class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}

        for n in nums:
            freqMap[n] = freqMap.get(n, 0) + 1
        
        items = list(freqMap.items())
        items.sort(key=lambda x: (x[1], x[0]), reverse=True)

        return [items[i][0] for i in range(k)]