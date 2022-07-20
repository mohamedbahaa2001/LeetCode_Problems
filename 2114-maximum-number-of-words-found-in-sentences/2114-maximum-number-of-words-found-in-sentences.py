class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxi = 0
        for i in sentences:
            maxi = max(len(list(i.split(' '))),maxi)
        return maxi