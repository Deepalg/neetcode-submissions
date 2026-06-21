import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        freq_map = defaultdict(int)
        heap = []
        result= []
        
        for i in range(length):
            freq_map[nums[i]]+=1

        for i in freq_map:
            heapq.heappush_max(heap, (freq_map[i],i))

        
        for i in range(k):
            result.append(heapq.heappop_max(heap)[1])

        return result            
        



        