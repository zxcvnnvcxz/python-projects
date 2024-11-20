from collections import defaultdict

from Tools.scripts.generate_opcode_h import header
from numpy.ma.core import minimum

from LeetCode.binarySearch import nums1


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hash = {}
        for i in nums:
            if i in hash:
                hash[i] += 1
                if hash[i] >= 2:
                    return True
            else:
                hash[i] = 1
        return False


solution = Solution()

print(solution.containsDuplicate([1,2,3,4,4]))
