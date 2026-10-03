class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hasht = {}
        for i in nums:
            hasht[i] = 1+ hasht.get(i,0)
        
        heap = []
        for f in hasht.keys():
            heapq.heappush(heap,(hasht[f],f))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res