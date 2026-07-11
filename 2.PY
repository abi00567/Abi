#2.first missing positive(leetcode-41)
def firstMissingPositive(nums):
    n = len(nums)

    # Place every number in its correct position
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
            nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

    # Find the first missing positive number
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    # If all numbers are present
    return n + 1

nums = [3, 4, -1, 1]
print(firstMissingPositive(nums))