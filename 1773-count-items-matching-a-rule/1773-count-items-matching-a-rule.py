class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        idx = 0
        count = 0
        if ruleKey == 'type':
            idx = 0
        elif ruleKey == 'color':
            idx = 1
        elif ruleKey == 'name':
            idx = 2
        for i in items:
            if i[idx] == ruleValue:
                count += 1
        return count