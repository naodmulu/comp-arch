class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        ans = []
        if num%3 == 0:
            middle = num//3
            left = middle -1
            right = middle +1

            ans = [left,middle,right]
        return ans
                
            
        