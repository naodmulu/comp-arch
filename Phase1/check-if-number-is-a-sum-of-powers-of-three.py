class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        powers = 15
        while powers >=0:
            x = 3**powers
            if x <= n:
                n -= x
            if n == 0:
                return True
            powers -=1
        return False


            


        