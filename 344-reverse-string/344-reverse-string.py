class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        # s[::-1]
        # n = len(s)
        # for i in range(n-1):
        #     s[i],s[n - 1 - i] = s[n - 1 - i], s[i]
        # print(s)