"""
Merge Sort方法。构建一个sums数组，对它进行merge sort，在merge的过程中抽取解。具体分析可见Xuan's blog，说得非常清楚明白。
这里简单记录一下思路：在合并sums[left:mid]和sums[mid+1:right]时，两个数组分别已经是有序的，
因此可以使用两指针的方法，对于左数组中的每一个元素，在右数组中寻找rl、rr
rl：对于左数组中的sums[i]，右数组中第一个不满足sums[rl] - sums[i] < lower的位置；
rr：对于左数组中的sums[i]，右数组中第一个不满足sums[rr] - sums[i] <= upper的位置；
那么rr-rl就是右数组元素减sums[i]在[lower，upper]中的个数。
由于两数组都是递增的，左数组向右移动的过程中，右数组的rl、rr指针也是向右移动的，不会回溯，因此合并部分的复杂度是O(n)。
"""
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        sums = [0]
        for num in nums:
            sums.append(sums[-1]+num)
        return self.helper(sums, lower, upper, 0, len(sums))
    
    def helper(self, sums, lower, upper, l, r):
        mid = (l+r)/2
        if mid == l:
            return 0
        count = self.helper(sums, lower, upper, l, mid) + self.helper(sums, lower, upper, mid, r)
        i = j = mid
        for left in sums[l: mid]:
            while i < r and sums[i] - left < lower:
                i += 1
            while j < r and sums[j] - left <= upper:
                j += 1
            count += j - i
        sums[l:r] = sorted(sums[l:r])
        return count
        
        
        
