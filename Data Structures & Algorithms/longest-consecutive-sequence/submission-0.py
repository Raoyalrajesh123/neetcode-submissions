class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash=set(nums)
        max=0
        for i in nums:
            count=1
            if i+1 not in hash:
                x=i
                while x-1 in hash:
                    count+=1
                    x=x-1
            if count>max:
                max=count
        return max