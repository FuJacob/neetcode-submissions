class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        target = len(nums) // 3
        ans = []
        for num, count in freq.items():
            if count > target:
                ans.append(num)
        return ans
