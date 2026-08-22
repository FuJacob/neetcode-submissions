class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ## if even: middle idxes, == (m+n - 1) // 2, then idx + 1 
        # if odd: middle = (m+n) // 2
        l, r = 0, 0
        m,n = len(nums1), len(nums2)
        ans = []
        while l < m or r < n:
            if l >= m:
                ans.extend(nums2[r:])
                break
            if r >= n:
                ans.extend(nums1[l:])
                break
            if nums1[l] < nums2[r]:
                ans.append(nums1[l])
                l+=1
            else:
                ans.append(nums2[r])
                r+=1
        ## then gra the middle
        middle = (m+n - 1) // 2
        if (m + n) % 2 == 0:
            return (ans[middle] + ans[middle+1]) / 2
        return ans[middle]




