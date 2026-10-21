class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in numToIndex:
                return [numToIndex[diff], i]
            numToIndex[n] = i