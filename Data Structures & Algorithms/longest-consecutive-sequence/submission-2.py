class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        num_set=set(nums)
        max_length=1

        for i, num in enumerate(nums):
            length=1
            while (num+1) in num_set:
                length+=1
                max_length=max(length,max_length)
                num=num+1

        return max_length

            

        