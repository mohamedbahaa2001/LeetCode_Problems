from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # count = 0
        sorted_arr = SortedList(nums)
        ans = []
        for i in nums:
            indx = sorted_arr.index(i)
            # small = nums[i+1:]
            # for j in small:
            #     if j < nums[i]:
            #         count += 1
            ans.append(indx)
            sorted_arr.remove(i)
            # count = 0
        return ans