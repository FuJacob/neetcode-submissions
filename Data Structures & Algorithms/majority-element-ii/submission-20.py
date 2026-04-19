class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        target = len(nums) // 3
        cand1 = cand2 = None
        count1 = count2 = 0
        for num in nums:
            if num == cand1:
                count1+=1
            elif num == cand2:
                count2+=1
            elif cand1 is None or count1 == 0:
                cand1 = num
                count1 = 1
            elif cand2 is None or count2 == 0:
                cand2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        ans = []
        f_count1 = f_count2 = 0
        for num in nums:
            if num == cand1:
                f_count1 +=1
            elif num == cand2:
                f_count2 +=1
        if f_count1 > target:
            ans.append(cand1)
        if f_count2 > target:
            ans.append(cand2)
        return ans




