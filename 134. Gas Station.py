class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start = len(gas) - 1
        end = 0
        total = gas[start] - cost[start]
        while end < start:
            if total < 0:
                start -= 1
                total += gas[start] - cost[start]
            else:
                total += gas[end] - cost[end]
                end += 1
        return start if total >= 0 else -1
