class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[]
        suffix=[]
        product=1
        product1=1
        m=[]
        for i in nums:
            prefix.append(product)
            product*=i
        for i in range(len(nums)-1,-1,-1):
            suffix.append(product1)
            product1*=nums[i]
        suffix.reverse()
        for i in range(len(nums)):
            m.append(prefix[i]*suffix[i])
        return m