from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num_dict=Counter(nums)
        n=len(nums)
        threshold=n/3
        res=[]
        for key,value in num_dict.items():
            if value >threshold:
                res.append(key)

        return res


        