class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        while l <= r:
            m_idx = l + (r - l) // 2
            m = nums[m_idx]
            if m == target: return m_idx
            if m < target:
                l = m_idx + 1
            else:
                r = m_idx - 1
        return -1
