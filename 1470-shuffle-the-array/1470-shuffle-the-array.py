class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = nums[:n]
        y = nums[n:]
        size = len(nums)
        nums.clear()
        for i,v in zip(x,y):
            nums.append(i)
            nums.append(v)
        return nums