def longestCharacter(s: str, k: int):
    count = {}
    max_freq = 0
    left = 0
    max_length = 0

    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1

        max_freq = max(max_freq, count[s[right]])

        if (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)
    return max_length

s = "ABAB"
k = 2
print(longestCharacter(s, k))  # Output: 4 ("ABAB" -> "AAAA" or "BBBB")

# # Example 2
# s = "AABABBA"
# k = 1
# print(characterReplacement(s, k))
