class Solution:
    def isPalindrome(self, x: int) -> bool:
        total = str(x)
        # total = map(int,total)
        total = list(total)
        rev = total[::-1]
        if total == rev:
            return True
        