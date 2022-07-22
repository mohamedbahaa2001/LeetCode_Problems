class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        return [True if (candies[i]+extraCandies) >= m else False for i in range(len(candies))]