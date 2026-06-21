from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt1=cnt2=0
        num1=num2=float("-inf")
        threshold = (len(nums)+3)//3
        res=[]
        for num in nums:
            if num==num1:
                cnt1+=1
            elif num==num2:
                cnt2+=1
            elif cnt1==0:
                num1=num
                cnt1+=1
            elif cnt2==0:
                num2=num
                cnt2+=1
            else:
                cnt1-=1
                cnt2-=1
            
        cnt1=cnt2=0
        for num in nums:
            if num ==num1:
                cnt1+=1
            elif num == num2:
                cnt2+=1
        
        if cnt1>=threshold:
            res.append(num1)
        if cnt2>=threshold:
            res.append(num2)

        return res
        