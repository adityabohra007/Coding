class Solution:
    """
    @param setList: The input set list
    @return: the cartesian product of the set list
    """
    def getSet(self, setList):
        # Write your code here
        self.result = []
        if setList is None or len(setList) == 0:
            return self.result
        self.helper(setList, [], 0)
        return self.result
    
    def helper(self, list, tmp, index):
        if index == len(list):
            self.result.append(tmp)
            return
        for i in xrange(len(list[index])):
            self.helper(list, tmp+[list[index][i]], index+1)
