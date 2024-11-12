# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n  # Start the search range from 1 to n

        while left < right:  # While there is more than one element to check
            mid = left + (right - left) // 2  # Find the middle version

            if isBadVersion(mid):  # If the middle version is bad
                right = mid  # The first bad version must be at mid or before mid
            else:
                left = mid + 1  # If mid is not bad, the first bad version must be after mid

        # At the end of the loop, left == right, which is the first bad version
        return left


nums = [1, 2, 3]