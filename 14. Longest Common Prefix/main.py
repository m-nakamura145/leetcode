class Solution:
    def longestCommonPrefix(self, strs):
        res = ""
        check = sorted(strs, key = lambda x: len(x))
        prefix = check[0]
        for i in range(len(prefix)):
            flag = 0
            for j in strs:
                if j[i] != prefix[i]:
                    flag = 1
                    break
            if flag == 0:
                res += prefix[i]
            else:
                return res
        return res
