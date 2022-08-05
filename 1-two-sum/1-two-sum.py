class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d: dict = {}
        for i in range(len(nums)):
            if target - nums[i] in list(d.keys()):
                return [i, d.get(target - nums[i])]
            d[nums[i]] = i