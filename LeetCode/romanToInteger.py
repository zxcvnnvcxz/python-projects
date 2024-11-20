class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        i = len(s) - 1

        while i > 0:
            i2 = values.get(s[i-1])
            i1 = values.get(s[i])
            if i2 < i1:
                total += i1 - i2
                i -= 2
            else:
                total += i1
                i -=1

        if i != -1:
            total += values.get(s[0])
        return total

class Solution:
    def romanToInt1(self, s: str) -> int:
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0

        for i in range(len(s)):
            if i+1 < len(s) and values[s[i]] < values[s[i+1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        return total

solution = Solution()
s = "III"
s1 = "MCMXCIV"
    #0123456
# 1000 - 100 + 1000 - 10 + 100 - 1 + 5
# Have a dictionary of replacement values.

print(solution.romanToInt1(s1))