#2.substring with concatenation(leetcode-30)
from collections import Counter
def findSubstring(s, words):
   # If string or words list is empty
    if not s or not words:
        return []

    # Length of one word
    word_len = len(words[0])

    # Total length of all words
    total_len = word_len * len(words)

    # Count frequency of words
    word_count = Counter(words)

    # Store result indices
    result = []

    # Check every possible starting position
    for i in range(len(s) - total_len + 1):

        # Dictionary for current window
        seen = {}

        # Check each word in the window
        for j in range(len(words)):

            # Extract one word
            word = s[i + j * word_len : i + (j + 1) * word_len]

            # If word exists in list
            if word in word_count:

                # Count occurrences
                seen[word] = seen.get(word, 0) + 1

                # If word appears too many times
                if seen[word] > word_count[word]:
                    break
            else:
                # Invalid word
                break

        # If all words matched
        if seen == word_count:
            result.append(i)

    return result


# Driver code
s = input("Enter string: ")
words = input("Enter words separated by space: ").split()

print("Starting Indices:", findSubstring(s, words))
