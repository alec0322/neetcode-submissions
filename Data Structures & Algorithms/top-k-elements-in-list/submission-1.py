class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}

        for n in nums:
            freqMap[n] = freqMap.get(n, 0) + 1
        
        items = list(freqMap.items())
        max_heap = [(-item[1], item[0]) for item in items]
        heapq.heapify(max_heap)

        res = []
        for i in range(k):
            freq, n = heapq.heappop(max_heap)
            res.append(n)
        
        return res