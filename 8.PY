3.# Regular Expression Matching leetcode(-10)
def isMatch(s, p):
    if p == ".*":      # Matches any string
        return True
    return s == p      # Exact match

# Driver code
s = input("Enter string: ")
p = input("Enter pattern: ")

if isMatch(s, p):
    print("Matched")
else:
    print("Not Matched")