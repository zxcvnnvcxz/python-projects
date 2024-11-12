class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        hash = {}

        for i in nums:
            if hash.get(i) is None:
                hash[i] = 0
            else:
                hash[i] += 1

        return max(hash, key=hash.get)


# Optimized Space Solution
class Solution:
    def majorityElement1(self, nums: list[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

solution = Solution()
print(solution.majorityElement1([3,3,2,3,2]))