class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        z=[]
        max1=0
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        for j in range(k):
            max = 0
            for i in dict:
                if dict[i] > max:
                    max = dict[i]
                    y=i
            z.append(y)
            del dict[y]
        return z