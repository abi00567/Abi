1.#mimimum window substring(leetcode-76)
from collections import Counter
def minWindow(s, t):
 # Count characters in t
    need = Counter(t)

    # Number of characters still needed
    missing = len(t)

    left = 0
    start = 0
    min_len = float("inf")

    # Move right pointer
    for right in range(len(s)):

        # If current character is needed
        if need[s[right]] > 0:
            missing -= 1

        # Reduce count
        need[s[right]] -= 1

        # If all characters are found
        while missing == 0:

            # Update minimum window
            if right - left + 1 < min_len:
                start = left
                min_len = right - left + 1

            # Remove left character
            need[s[left]] += 1

            # If removed character is required
            if need[s[left]] > 0:
                missing += 1

            # Move left pointer
            left += 1

    # Return result
    if min_len == float("inf"):
        return ""

    return s[start:start + min_len]


# Driver code
s = input("Enter string: ")
t = input("Enter target: ")

print("Minimum Window:", minWindow(s, t))

