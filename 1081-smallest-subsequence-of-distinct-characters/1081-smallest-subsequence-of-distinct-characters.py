class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        vis = [False]*26
        last = [-1]*26
        l = len(s)
        st = []
        for i in range(l) :
            last[ord(s[i]) - ord('a')] = i
        for i in range(l) :
            if vis[ord(s[i]) - ord('a')] == False : 
                while st :
                    if ord(st[-1]) > ord(s[i]) and last[ord(st[-1]) - ord('a')] > i :
                        vis[ord(st[-1]) - ord('a')] = False
                        st.pop()
                    else : break
                st.append(s[i])
                vis[ord(s[i]) - ord('a')] = True
        return ''.join(st)
                