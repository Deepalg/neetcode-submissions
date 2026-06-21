class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        num_set=set(nums)
        max_length=1

        for i, num in enumerate(nums):
            if (num-1) not in num_set:
                length=1
                while (num+length) in num_set:
                    length+=1
                max_length=max(length,max_length)
        return max_length

            

        