import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <=1:
            return nums
        
        map = defaultdict(int)
        for num in nums:
            map[num] += 1
        heap = []
        for key, value in map.items():
            heapq.heappush(heap, (-value,key))
        res=[]
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        print(res)
        return res

        



        