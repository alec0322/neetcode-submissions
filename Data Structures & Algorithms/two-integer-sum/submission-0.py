class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        for i, n in enumerate(nums):
            if n in freq:
                return [freq[n], i]
            diff = target - n
            freq[diff] = i