#3.Sliding window maximum(leetcode-239)
def maxSlidingWindow(nums, k):
    result = []

    # Move the window from left to right
    for i in range(len(nums) - k + 1):

        # Find maximum element in current window
        result.append(max(nums[i:i+k]))

    return result

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

print(maxSlidingWindow(nums, k))