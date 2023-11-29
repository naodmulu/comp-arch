class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or strs ==[""]:
            return("")
        for i in range(len(strs[0])):
            check = strs[0][0:i+1]
            print(check)    
            for j in range(len(strs)):
                if check == strs[j][0:i+1] and strs[j][0:i+1] :
                    continue
                return check[0:i]
        return strs[0]

#strs = ["flower","flow","flight"]
#         ^
#         ^



        