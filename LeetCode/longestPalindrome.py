from collections import defaultdict


class Solution:
    def longestPalindrome(self, s:str) -> int:
        seen = set()
        result = 0

        for c in s:
            if c in seen:
                seen.remove(c)
                result += 2
            else:
                seen.add(c)

        if seen:
            result += 1

        return result