class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        alph = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
        nums = [1,2,3,4,5,6,7,8]

        a = alph[coordinates[0]]
        n = int(coordinates[1])
        s = int(a) + n
        if s%2 == 0 :
            return False
        else:
            return True
        