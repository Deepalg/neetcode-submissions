import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        freq_map = defaultdict(int)
        bucket_sort = [[] for _ in range(length)]
        result= []
        
        for i in range(length):
            freq_map[nums[i]]+=1

        for i in freq_map:
            bucket_sort[freq_map[i]-1].append(i)

        l=length-1
        while k>0:
            if len(bucket_sort[l])>0:
                result.append(bucket_sort[l].pop())
                k-=1
            else:
                l-=1
        return result

                   
        



        