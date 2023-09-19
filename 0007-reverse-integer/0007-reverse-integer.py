class Solution:
    def reverse(self, x: int) -> int:
        res = ""
        x_str = str(x)
        
        if (x == 0):
            return 0
        
        for i in range(len(x_str)-1, -1, -1):
            if (i == len(x_str) - 1) and (x_str[i] == "0"):
                continue

            elif (i == 0) and (x_str[i] == "-"):
                res = "-" + res
                continue

            else:
                res += x_str[i]

        res = int(res)

        if (res <= (-2)**31) or (res >= (2)**31 - 1):
            return 0
        else:
            return res        
        