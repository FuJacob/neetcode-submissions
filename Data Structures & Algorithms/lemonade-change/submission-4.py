class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5:0, 10: 0, 20:0}
        for bill in bills:
            if bill == 5:
                change[bill] += 1
                continue
            diff = bill - 5
            for change_bill in [10,5]:
                if change_bill > diff or change[change_bill] == 0:
                    continue
                while diff - change_bill >= 0 and change[change_bill] > 0:
                    diff -= change_bill
                    change[change_bill] -= 1
            if diff != 0:
                return False
            change[bill] += 1
        return True