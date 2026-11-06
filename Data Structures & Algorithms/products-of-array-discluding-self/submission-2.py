class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        prefix = 1
        for n in nums:
            products.append(prefix)
            prefix *= n
        
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            products[i] *= suffix
            suffix *= nums[i]
        
        return products