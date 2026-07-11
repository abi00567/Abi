5.# Distinct Subsequences leetcode(115)
def numDistinct(s, t):

    # If target is not in string
    if t in s:
        return 1
    else:
        return 0

# Driver code
s = input("Enter string: ")
t = input("Enter target: ")

print("Count:", numDistinct(s, t))