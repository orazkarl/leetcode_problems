class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        length_nums = len(nums)
        if length_nums % 2 == 0:
            return (nums[length_nums // 2 ] + nums[length_nums // 2 - 1]) / 2
        return nums[length_nums // 2 ]