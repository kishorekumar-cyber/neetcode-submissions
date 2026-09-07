class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashpmap={}
        for i,n in enumerate(nums):
            diff= target- n
            if diff in hashpmap:
                return [hashpmap[diff],i]
            hashpmap[n]=i
        

        