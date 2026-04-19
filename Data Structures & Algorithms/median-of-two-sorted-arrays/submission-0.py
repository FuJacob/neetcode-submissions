class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n = len(nums1), len(nums2)
        arr = nums1 + nums2
        arr.sort()
        if len(arr) % 2 == 0:
            idx = math.floor((len(arr) - 1) / 2)
            return (arr[idx] + arr[idx+1]) / 2
        return arr[math.floor((len(arr) - 1) / 2)]


