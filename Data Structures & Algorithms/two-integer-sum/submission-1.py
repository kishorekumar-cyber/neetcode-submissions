class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i , m in enumerate(nums):
            n = target - nums[i]
            if n in hashmap:
                return [hashmap[n],i]
            hashmap[m] =i