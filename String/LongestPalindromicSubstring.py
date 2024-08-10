

def LongestPalindromicSubstring(s):
    def expand(left,right):
        while left>=0 and right<len(s) and s[right]==s[left]:
            left-=1
            right+=1

        return s[left+1:right]

    longest=""

    for i in range(len(s)):
        odd_pali=expand(i,i)
        even_pali=expand(i,i+1)
        longest=max(longest,odd_pali,even_pali,key=len)
    return longest

print(LongestPalindromicSubstring("abbauend"))
