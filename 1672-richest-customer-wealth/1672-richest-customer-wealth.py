class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sm = 0
        maxi = 0
        for i in accounts:
            sm = sum(i)
            maxi = max(sm,maxi)
        return maxi