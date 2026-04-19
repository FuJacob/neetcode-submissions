class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        m,n = len(A), len(B)
        half = (m + n + 1) // 2
        l, r = 0, m
        while l <= r:
            pivot = l + (r - l) // 2 ## idx
            pivot_b = half - pivot ## this is where cut off from nums2
            A_left = A[pivot-1] if 0 < pivot else float('-infinity')
            A_right = A[pivot] if m > pivot else float('infinity')
            
            B_left = B[pivot_b-1] if 0 < pivot_b else float('-infinity')
            B_right = B[pivot_b] if n > pivot_b else float('infinity')
            
            if A_left <= B_right and B_left <= A_right:
                max_left = max(A_left, B_left)
                
                if (m+n) % 2 == 1:
                    return float(max_left)
                
                min_right = min(A_right, B_right) ## the amx left and min right

                return (max_left + min_right) / 2
            elif A_left > B_right:
                r = pivot
            elif B_left > A_right:
                l = pivot+1
        return l



            
