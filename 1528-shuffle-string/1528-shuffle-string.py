class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [x for x in range(len(s))]
        stri = ''
        for i in range(len(s)):
            ans[indices[i]] = s[i]
        for i in ans:
            stri += i
        return stri
            
            
            