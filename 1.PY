1.#trapping rain water (leetcode-42)
def trap(height):
    n = len(height)

    # Create arrays to store left and right maximum heights
    left = [0] * n
    right = [0] * n

    # Store maximum height from the left
    left[0] = height[0]
    for i in range(1, n):
        left[i] = max(left[i-1], height[i])

    # Store maximum height from the right
    right[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        right[i] = max(right[i+1], height[i])

    # Calculate trapped water
    water = 0
    for i in range(n):
        water += min(left[i], right[i]) - height[i]

    return water

height = [3, 0, 2, 0, 4]
print(trap(height))