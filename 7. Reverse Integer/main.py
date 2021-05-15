class Solution:
    def reverse(self, x):
        result = 0
        if(x == 0):
            return result
        string_x = str(x)
        if(string_x[0] == '-'):
            result = -int(string_x[:0:-1])
        else:
            result = int(string_x[::-1])
        if(not (result in range(-2 ** 31, 2 ** 31 - 1))):
            return 0
        else:
            return result
