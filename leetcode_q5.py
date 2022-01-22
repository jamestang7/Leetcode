
def longestPalindrome(s):
    result = ""
    def helper(s, l, r):
        # return the longest Pal from inner to outer
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1: r]
    
    for i in range(len(s)):
        # odd case
        temp = helper(s, i, i)
        if len(temp) > len(result):
            result = temp
        temp = helper(s, i ,i + 1)
        if len(temp) > len(result):
            result = temp
    return result 

# Driver program to test above functions
seq = "aacabdkacaa"
print(longestPalindrome(seq))

