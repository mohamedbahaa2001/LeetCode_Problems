class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        
        ans = [1]
        while len(ans) < n:
            res = []
            for el in ans:
                if 2 * el - 1 <= n:
                    res.append(el * 2 - 1)

            for el in ans: 
                if 2 * el <= n:
                    res.append(el * 2)

            ans = res
        return ans
