class Solution(object):
    def twoSum(self, numbers, target):
        lo, hi = 0, len(numbers) - 1

        while lo < hi:
            total = numbers[lo] + numbers[hi]
            if total == target:
                return [lo + 1, hi + 1]
            elif total < target:
                lo += 1
            else:
                hi -= 1
        return []