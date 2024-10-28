def twoSum(nums: list[int], target: int) -> list[int]:
    total = None
    x = 0
    y = x + 1
    while total != target:
        numbers = [nums[x], nums[y]]
        total = sum(numbers)
        y = y + 1
        if total == target:
            return x, y - 1
        if y >= len(nums):
            x = x + 1
            y = x + 1



print(twoSum(nums=list(range(0, 1000000)), target=782347))