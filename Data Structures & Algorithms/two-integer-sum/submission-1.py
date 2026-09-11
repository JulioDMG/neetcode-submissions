class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #dictionary
        for i ,num in enumerate(nums): #enumerate asigns index to i and nums to num
            difference = target - num
            if difference in seen:
                return [seen[difference],i]
            seen[num] = i
