class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:

        # [nums[2*i], nums[2*i+1]]
        #    freq       val
        ans = []
        if len(nums) == 2:
            freq = nums[0]
            val = nums[1]
            ans.extend([val for i in range(freq)])
        else:
            for i in range(0,len(nums),2):
                freq = nums[i]
                val = nums[i+1]
                ans.extend([val for i in range(freq)])
        return ans