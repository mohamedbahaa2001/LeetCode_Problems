class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        summ = 0
        ans = []
        for i in range(len(nums)):
            summ +=  int(nums[i])
            ans.append(summ)
        return ans