class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        p = 1
        for n in nums:
            prefix.append(p)
            p *= n
        
        s = 1
        for i in range(len(nums)-1, -1, -1):
            prefix[i] *= s
            s *= nums[i]
        
        return prefix