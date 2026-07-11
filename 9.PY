#4.Palindrome partition leetcode(-132)
def partition(s):
    if s == s[::-1]:      # Check palindrome
        return [[s]]
    return [[c for c in s]]   # Split into characters

# Driver code
s = input("Enter string: ")
print(partition(s))
