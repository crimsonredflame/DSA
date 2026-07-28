class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = [0]*26
        for i in range(len(s)) :
            arr[ord(s[i])-ord('a')] += 1
        res = ''
        for i in range(26):
            res += chr(i + ord('a')) * (arr[i] // 2)
        idx = len(res)
        for i in range(26) :
            if arr[i] > 0 and arr[i]%2 == 1:
                res += (chr(i+ord('a')))
                break
        res += res[:idx][::-1]
        return res